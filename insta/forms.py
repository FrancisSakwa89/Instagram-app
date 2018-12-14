from django import forms
from .models import Image,Comment,Profile,Likes

class NewImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['poster','postername', 'pub_date']


class NewCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['image_id','postername','pub_date']



class NewProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']
class InstaLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')