from django.db import models

# Create your models here.
class Image(models.Model):
   Image = models.ImageField(upload_to = 'insta/')
   Image_name = models.CharField(max_length =30)
   Image_caption = models.TextField(max_length =40)
   Likes = models.CharField(max_length =20,blank =True)
   profile = models.ForeignKey(Profile, null = True,related_name='image')
   pub_date = models.DateTimeField(auto_now_add=True, null=True)
   comment = models.ForeignKey
   user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)