from django.shortcuts import render,redirect
from .models import Image, Profile,Like
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import InstaLetterForm
from .models import InstaLetterRecipients
# Create your views here.
def welcome(request):
    if request.method == 'POST':
        form = InstaLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index.html')
    else:
        form = InstaLetterForm()
    return render(request, 'index.html', {"letterForm":form})
    
def like(request, picture_id):
    new_like, created = Like.objects.get_or_create(user=request.user, picture_id=picture_id)

def picture_detail(request, id):
    pic = get_object_or_404(Picture, pk=id)
    user_likes_this = pic.like_set.filter(user=request.user) and True or False    

