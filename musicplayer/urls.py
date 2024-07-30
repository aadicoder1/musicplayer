from django.contrib import admin
from django.urls import path, include

from musicplayer.settings import MEDIA_ROOT
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('echo/', include('echo.urls'))
    
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)






