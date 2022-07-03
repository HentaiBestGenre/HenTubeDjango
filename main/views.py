from django.shortcuts import render
from Videos.models import Video

def main_page(request):
    videos = Video.objects.order_by('-pub_data')[:10]
    return render(request, "main.html", {"videos":videos})
