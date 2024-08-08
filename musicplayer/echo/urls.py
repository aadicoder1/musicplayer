from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from musicplayer.settings import MEDIA_ROOT
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('songs',views.songs, name='songs'),
    path('songs/<int:song_id>',views.songpost, name='songpost'),
    path('liked_songs',views.liked_songs, name='liked_songs'),
    path("liked/<int:song_id>", views.liked, name="liked"),
    path('search',views.search, name='search'),
    
    path("profile/", views.profile, name="profile"),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


