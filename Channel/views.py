from django.shortcuts import render
from django.contrib.auth.models import User
from Videos.models import Video
from .models import Chanel
from django.http import Http404

def channel(request, user_id):
    try:
        chanel = Chanel.objects.get(pk=user_id)
        videos = Video.objects.filter(creater_id=user_id)
    except:
        raise Http404("Chanel not found")
    return render(request, 'Index.html', {'data': chanel, 'videos': videos})
