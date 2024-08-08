from django.shortcuts import render,redirect
from echo.models import Song,Profile

# Create your views here.


def index(request):
    user = request.user    
    print(user.first_name)
    song=Song.objects.all()
    return render(request,'index.html',{'song':song , "user":user} )


def songs(request):
    song=Song.objects.all()
    return render(request,'songs.html',{'song':song})


def songpost(request,song_id):
    song=Song.objects.get(id=song_id)
    return render(request, 'songpost.html', {'song':song})


def liked_songs(request):
    
    user=request.user
    print(f"Current User: {user}")
    liked_song=[]
    songs=Song.objects.filter(is_liked = True, user = user)
    print(f"Liked Songs Queryset: {songs}")
    #for song in songs:
    #    if song.is_liked==True:
    #        liked_song.append(song)
    #user_liked_song=liked_song
    parameters={'songs':songs, #'user_liked_song':user_liked_song
                }
    return render(request,'liked_songs.html' ,parameters)


def liked(request,song_id):
    song= Song.objects.get(id=song_id)
    song.is_liked = not song.is_liked
    song.save()
    return render(request,'songpost.html',{'song':song})


def search(request):
    query=request.GET.get("query")
    if not query:
        return render(request, 'search.html', {'song': []})
    
    song=Song.objects.all()
    qs=song.filter(name__icontains=query) #qs=query set
    return render(request, 'search.html', {'song':qs})


def profile(request):
    
    if request.method == "POST":
        profile_pic=request.FILES["profile_pic"]
        
        new_profile=Profile(
            title="Profile pic",
            profile_pic=profile_pic
        )        
        new_profile.save()
        return redirect("profile")
        
    return render(request, "profile.html")
