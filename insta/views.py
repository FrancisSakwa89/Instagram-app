from django.shortcuts import render,redirect
from .models import Image, Profile, Comment, Likes, Follow,InstaLetterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import InstaLetterForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.core.exceptions import ObjectDoesNotExist
from .forms import ImageForm, CommentForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    id = request.user.id
    profile = Profile.objects.get(user=id)
    images = Image.objects.all()
    # if request.method == 'POST':
    #     form = InstaLetterForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']
    #         email = form.cleaned_data['email']
    #         recipient = InstaLetterRecipients(name = name,email =email)
    #         recipient.save()
    #         send_welcome_email(name,email)
    #         HttpResponseRedirect('index.html')
    # else:
    #     form = InstaLetterForm()
    return render(request, 'index.html', {'images':images,'profile':profile})
    
def like(request, picture_id):
    new_like, created = Like.objects.get_or_create(user=request.user, picture_id=picture_id)

def picture_detail(request, id):
    pic = get_object_or_404(Picture, pk=id)
    user_likes_this = pic.like_set.filter(user=request.user) and True or False    

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
    message = 'You haven\'t searched for any user'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})

def subscribe(request):
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
    return render(request, 'subscribe.html', {'letterForm':form})
def newimage(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  current_user = request.user
  current_username = request.user.username
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.save(commit=False)
      image.poster = current_user
      image.postername = current_username
      image.save()
    return redirect('welcome')

  else:
    form = ImageForm()

  return render(request, 'newimage.html',{'form':form,'profile':profile})



def newcomment(request,id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  id = id

  current_username = request.user.username
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.postername = current_username
      comment.image_id = Image.objects.get(pk=id)
      comment.save()
    return redirect('image',id)

  else:
    form = CommentForm()

  return render(request, 'comment.html',{'form':form,'profile':profile,'id':id})



@login_required(login_url='/accounts/login/')
def profile(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  user = request.user
  
  myprofile = Profile.objects.get(pk=id)

  follows = Follow.objects.filter(follows=frank)
  following = follows.count()
  followed = Follow.objects.filter(followed=frank)
  followers = followed.count()
  images = Image.objects.filter(poster=frank)
  photocount=images.count()


  return render(request, 'profile.html',{'myprofile':myprofile,'profile':profile,'user':user,'following':following,'followers':followers,'photocount':photocount,'images':images})



@login_required(login_url='/accounts/login/')
def image(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  
  image = Image.objects.get(pk=id)
  comments = Comment.objects.filter(image_id=id)

  user = request.user
  image = Image.objects.get(pk=id)

  like = Likes.objects.filter(user=user,image=image)
  rows = like.count()


  return render(request, 'image.html',{'profile':profile,'image':image,'comments':comments, 'rows':rows})



@login_required(login_url='/accounts/login/')
def like(request, id):
  user = request.user
  image = Image.objects.get(pk=id)

  rows = Likes.objects.filter(user=user,image=image)

  if rows.count() == 0:
    like = Likes(user=user,image=image)
    like.save()

  else:
    rows.delete()
  
  return redirect('image', id )



@login_required(login_url='/accounts/login/')
def follow(request, id):
  follows = request.user
  followed = User.objects.get(pk=id)

  rows = Follow.objects.filter(follows=follows,followed=followed)

  if rows.count() == 0:
    follow = Follow(follows=follows,followed=followed)
    follow.save()

  else:
    rows.delete()
  
  return HttpResponseRedirect(reverse('newprofile'))



@login_required(login_url='/accounts/login/')
def newprofile(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  # current_user = request.user
  # current_username = request.user.username
  
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=frank)
    form = ProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()
      # u_profile = form.save(commit=False)
      # u_profile.user = current_user
      # u_profile.save()

    return redirect('profile', frank)

  else:
    form = ProfileForm()

  return render(request, 'newprofile.html',{'form':form,'profile':profile})    