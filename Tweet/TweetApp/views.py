from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404
from .models import Profile, Tweet, Comment
from datetime import datetime

# Create your views here.
def index(request):
	# vehicles = Vehicle.objects.all()
	return render(request, 'tweets.html',{
		'tweets': Tweet.objects.all().order_by('-pub_date')
	}) 
	# return HttpResponse('My page')

def signup(request):
	# vehicles = Vehicle.objects.all()
	# return render(request, 'articles.html',{
	# 	'articles': Article.objects.all().order_by('-pub_date')
	# }) 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		bio = request.POST['bio']
		user = User.objects.create_user(username=username, password=password)
		if user is not None:
			user.save()
			profile = Profile(bio=bio, user=user)
			profile.save()
			login(request, user)
			return redirect('TweetApp:index')
	return render(request, 'signup.html')

def signin(request):
	# vehicles = Vehicle.objects.all()
	# return render(request, 'articles.html',{
	# 	'articles': Article.objects.all().order_by('-pub_date')
	# }) 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('index')
	return render(request, 'signin.html')

def signout(request):
	logout(request)
	return render(request, 'signin.html')

def profile(request):
	if request.user.is_authenticated:
		return render(request, 'profile.html', {'user': request.user})
	else:
		return render(request, 'signin.html')

def addtweet(request): 
	if request.method == 'POST':
		text_tweet = request.POST['tweet']
		pub_date = datetime.now()
		print(request.user)
		p = Profile.objects.get(user=request.user)
		t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
		t.save()
		return redirect('index')

