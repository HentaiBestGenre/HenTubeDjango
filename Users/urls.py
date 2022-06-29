from django.urls import path
from . import views

app_name = 'Users'
urlpatterns = [
    path('Login/', views.login_user, name='login'),
    path('Logout/', views.logout_user, name='logout'),
]