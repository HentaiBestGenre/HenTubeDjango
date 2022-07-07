from django.urls import path
from . import views

urlpatterns = [
    path('like/', views.like, name='like'),
    path('', views.index, name='index'),
    path('<video_id>/', views.video, name='video'),
    path('index2/', views.index2, name='index2'),
    path('posting/', views.post_video, name='post_video'),
    path('comment', views.comment, name='comment'),
]
app_name = 'Videos'
