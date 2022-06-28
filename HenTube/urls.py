from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Videos.urls')),
    # path('User/', include('Profiles.urls')),
    # path('Channel/', include('Channel.urls')),
]
