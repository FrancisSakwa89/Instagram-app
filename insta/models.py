from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
   Image = models.ImageField(upload_to = 'insta/')
   Image_name = models.CharField(max_length =30)
   Image_caption = models.TextField(max_length =40)
   Likes = models.CharField(max_length =20,blank =True)
   profile = models.ForeignKey(User, null = True,related_name='image')
   pub_date = models.DateTimeField(auto_now_add=True, null=True)
   comment = models.ForeignKey
#    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Profile(models.Model):
   Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
   Bio = models.TextField(max_length = 50)
#    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)   

class Like(models.Model):
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)
    created = models.DateTimeField(auto_now_add=True)
    # p = Profile.objects.get(...)
    # number_of_likes = p.like_set.all().count()    
class InstaLetterRecipients(models.Model):
   name = models.CharField(max_length = 30)
   email = models.EmailField()