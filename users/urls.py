from atexit import register
from django.urls import path,include
from users.views import Register,mtavari_viwe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registracia/',Register.as_view(), name='registracia'),
     path('mtvari/',mtavari_viwe, name='mtavari')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)