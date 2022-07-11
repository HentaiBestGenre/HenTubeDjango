from django.shortcuts import render
from Videos.models import Video
from .models import Chanel
from django.http import Http404

def channel(request, user_id):
    try:
        c = Chanel.objects.get(pk=user_id)
        v = Video.objects.filter(creater_id=user_id).order_by('-pub_data')
    except:
        return Http404
    return render(request, 'Index.html', {'channel': c, 'videos': v})
