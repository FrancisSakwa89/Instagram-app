from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
  photo = models.ImageField(upload_to = 'insta/',default='capture')
  bio = models.CharField(max_length=200,default='work')
  user = models.OneToOneField(User, on_delete=models.CASCADE,default='frank')

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  @classmethod
  def update_profile(cls,id,bio,photo):
    profile = cls.objects.get(pk=id)
    profile = cls(photo=photo,bio=bio)
    profile.save()



class Image(models.Model):
  image = models.ImageField(upload_to = 'photos/')
  name = models.CharField(max_length=60,default='people', blank=False, null=False)
  caption = models.TextField(default='myphoto', blank=False, null=False)
  poster = models.ForeignKey(User,on_delete=models.CASCADE, default='now')
  postername = models.CharField(max_length=60, default='me')
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  class Meta:
    ordering = ['name']

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls,id,name,caption):
    image = cls.objects.get(pk=id)
    image = cls(name=name,caption=caption)
    image.save()



class Comment(models.Model):
  comment = models.TextField(default='cool')
  image_id = models.ForeignKey(Image,on_delete=models.CASCADE)
  postername = models.CharField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)

  def save_comment(self):
    self.save()

  def delete_comment(self):
    self.delete()

  @classmethod
  def update_comment(cls,id,comment):
    comment = cls.objects.get(pk=id)
    comment = cls(comment=comment)
    comment.save()



class Likes(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='frank')
  image = models.ForeignKey(Image,on_delete=models.CASCADE, default='caption')



class Follow(models.Model):
  follows = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follows')
  followed = models.ForeignKey(User,on_delete=models.CASCADE, related_name='followed')

class InstaLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
