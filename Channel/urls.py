from django.urls import path
from . import views

app_name = 'Channels'
urlpatterns = [
    path('channel/<int:user_id>/', views.channel, name='channel'),
]