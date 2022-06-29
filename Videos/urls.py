from django.urls import path
from . import views

app_name = 'Videos'
urlpatterns = [
    path('', views.Index, name='index'),
    path('index2/', views.Index, name='index2'),
]