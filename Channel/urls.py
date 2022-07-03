from django.urls import path
from . import views

app_name = 'Channels'
urlpatterns = [
    path('<int:user_id>/', views.index, name='channel'),
]