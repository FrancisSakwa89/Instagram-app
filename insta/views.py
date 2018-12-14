from django.shortcuts import render,redirect
from .models import Image, Profile,Like
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import InstaLetterForm
from .models import InstaLetterRecipients
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def search_results(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  this_user = request.user.username

  if 'user' in request.GET and request.GET['user']:
    search_term = request.GET.get('user')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      searched_users = User.objects.filter(username__icontains = no_ws).exclude(username = this_user)

    except ObjectDoesNotExist:
      searched_users = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_users':searched_users,'profile':profile})

  else:
    message = 'You haven\'t searched for any users'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})
