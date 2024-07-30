from django.shortcuts import render
from echo.models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect

def index(request):
    song=Song.objects.all()
    return render(request,'echo/index.html',{'song':song} )

def songs(request):
    song=Song.objects.all()
    return render(request,'echo/songs.html',{'song':song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request, 'echo/songpost.html', {'song':song})

def login(request):
    return render(request, 'echo/login.html')

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        pass1=request.POST.get('pass1')
        
        myuser=User.objects.create_user(username=username,email=email,pass1=pass1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        user=authenticate(username=username,password=pass1)
        login(request,user)
        
        return redirect('/')
    return render(request, 'echo/signup.html')    