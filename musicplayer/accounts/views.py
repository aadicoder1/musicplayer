from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method=="POST":
        input_username= request.POST.get("username")
        input_password= request.POST.get("password")
        
        user=auth.authenticate(username=input_username , password=input_password)
        
        if user is not None:
            auth.login(request,user)
            return redirect ("index")
        
    return render(request,"accounts/login.html")



def signup(request):
    
    if request.method=="POST":
        input_username= request.POST.get("username")
        input_password= request.POST.get("password")
        input_firstname= request.POST.get("firstname")
        input_lastname= request.POST.get("lastname")
        input_email= request.POST.get("email")
    
        new_user=User(
            username = input_username,
            first_name=input_firstname,
            last_name=input_lastname,
            email=input_email,
        )
        new_user.set_password(input_password)
        
        new_user.save()
        return redirect("login")
    
    return render(request,"accounts/signup.html")

