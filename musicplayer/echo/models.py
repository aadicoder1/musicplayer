from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    name= models.CharField( max_length=2000)
    singer=models.CharField(max_length=200)
    tags=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    song= models.FileField( upload_to='images')
    
    is_liked= models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile_pic/")