from django.contrib import admin
from .models import Image, Profile,Likes

# Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =('profile',)

admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Image)