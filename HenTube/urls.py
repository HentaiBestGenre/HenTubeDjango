from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('Videos.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('Users.urls')),
    path('', include('main.urls')),
    # path('User/', include('Profiles.urls')),
    path('channel/', include('Channel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
