from django.urls import path
from . import views

app_name = 'Videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<video_id>/', views.video, name='video'),
    path('index2/', views.index2, name='index2'),
    path('posting/', views.post_video, name='post_video'),
]