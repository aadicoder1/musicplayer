from django.shortcuts import render
from echo.models import Song

def index(request):
    song=Song.objects.all()
    return render(request,'echo/index.html',{'song':song} )

def songs(request):
    return render(request,'echo/songs.html')