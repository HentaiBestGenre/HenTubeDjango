from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import UploadVideoForm
from django.http import Http404

@login_required(login_url='Users:login')
def index(request):
    return render(request, 'Videos/index.html', {})

@login_required(login_url='Users:login')
def index2(request):
    return render(request, 'Videos/index2.html', {})

def video(request, video_id):
    try:
        video = Video.objects.get(pk = video_id)
        return render(request, 'Videos/video.html', {'video': video})
    except:
        raise Http404


@login_required(login_url='Users:login')
def post_video(request):
    if request.method == "POST":
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['video']
            file.name = normalize_file_name(file.name)
            video = Video(
                title=request.POST["title"],
                creater=request.user,
                path_name = file.name
            )
            video.save()
            handle_uploaded_file(file, file.name)
            return redirect('Videos:index')
    return redirect('Videos:index')

def normalize_file_name(fn :str):
    """fn - file name, sfn - save file name"""
    salt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    sfn = fn.replace(' ', '_').replace('.', f'_{salt}.')
    return sfn

def handle_uploaded_file(f, fale_name):
    with open('media/' + fale_name, 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)

if __name__ == "__main__":
    file = "adad as qwe lf"
    normalize_file_name(file)
