from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video, Like, Comments
from .forms import UploadVideoForm, AddCommentForm
from django.http import Http404, JsonResponse

@login_required(login_url='Users:login')
def index(request):
    return render(request, 'Videos/index.html', {})

@login_required(login_url='Users:login')
def index2(request):
    return render(request, 'Videos/index2.html', {})

def video(request, video_id):
    try:
        video = Video.objects.get(pk = video_id)
        likes = Like.objects.filter(video_id = video_id, value=True).count()
        dislikes = Like.objects.filter(video_id = video_id, value=False).count()
        comments = Comments.objects.filter(video_id = video_id).order_by('-date')
        return render(request, 'Videos/video.html', {'video': video, 'likes': likes, 'dislikes': dislikes, 'comments': comments})
    except:
        raise Http404


@login_required(login_url='Users:login')
def post_video(request):
    if request.method == "POST":
        form = UploadVideoForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            v = request.FILES['video']
            v.name = normalize_file_name(v.name)
            p = request.FILES['preview']
            p.name = normalize_file_name(p.name)
            video = Video(
                title=request.POST["title"],
                creater=request.user,
                path_name = v.name,
                preview = p.name,
            )
            video.save()
            handle_uploaded_file(v, v.name, 'videos')
            handle_uploaded_file(p, p.name, 'previews')
            return redirect('Videos:index')
    return redirect('Videos:index')

@login_required(login_url='Users:login')
def like(request):
    value = True if request.POST['value'] == 'true' else False
    try:
        record = Like.objects.get(
            video_id=request.POST['video_id'],
            user_id=request.POST['user_id'],
        )
        if record.value is value:
            record.delete()
        else:
            record.value = value
            record.save()
    except:
        new_record = Like(
            video_id=request.POST['video_id'],
            user_id=request.POST['user_id'],
            value=value
        )
        new_record.save()
    likes = Like.objects.filter(video_id=request.POST['video_id'], value=True).count()
    dislikes = Like.objects.filter(video_id=request.POST['video_id'], value=False).count()
    return JsonResponse({'likes': likes, 'dislikes': dislikes}, status=200)

@login_required(login_url='Users:login')
def comment(request):
    form = AddCommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = Comments(
            user_id=request.POST['user_id'],
            video_id=request.POST['video_id'],
            value=request.POST['value'],
        )
        comment.save()
        return JsonResponse({'value': comment.value, 'username': comment.user.username}, status=200)

def normalize_file_name(fn :str):
    """fn - file name, sfn - save file name"""
    salt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    sfn = fn.replace(' ', '_').replace('.', f'_{salt}.')
    return sfn

def handle_uploaded_file(f, fale_name, type):
    with open(f'media/{type}/{fale_name}', 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
