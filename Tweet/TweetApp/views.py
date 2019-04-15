from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Tweet, Comment
from ProfileApp.models import Profile
from datetime import datetime

# Create your views here.
def index(request):
	# vehicles = Vehicle.objects.all()
	return render(request, 'tweets.html',{
		'tweets': Tweet.objects.all().order_by('-pub_date')
	}) 
	# return HttpResponse('My page')

def addtweet(request): 
	if request.method == 'POST':
		text_tweet = request.POST['tweet']
		pub_date = datetime.now()
		print(request.user)
		p = Profile.objects.get(user=request.user)
		t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
		t.save()
		return redirect('index')

def deletetweet(request, tweet_id): 
	print(request.method)
	if request.method == 'POST':
		# request.method -> DELETE
		t = get_object_or_404(Tweet, pk=tweet_id)
		t.delete()
		# text_tweet = request.POST['tweet']
		# pub_date = datetime.now()
		# print(request.user)
		# p = Profile.objects.get(user=request.user)
		# t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
		# t.save()
		return redirect('index')
	else:
		return redirect('index')


def addcomment(request, tweet_id): 
	t = Tweet.objects.get(pk=tweet_id)
	c = t.comment_set.all()
	if request.method == 'POST':
		text_comment = request.POST['comment']
		pub_date = datetime.now()
		p = Profile.objects.get(user=request.user)
		if p != None:
			c = Comment(text_comment=text_comment, pub_date=pub_date, 
			profile_comment=p, tweet_comment=t)
			print(c)
			c.save()
			return redirect('index')
		else:
			return redirect('index')
	else:
		return render(request, 'addcomment.html', { 'tweet_id':tweet_id, 
			'text': t.text_tweet, 'comments': c})

def deletecomment(request, comment_id): 
	if request.method == 'POST':
		c = get_object_or_404(Comment, pk=comment_id)
		c.delete()
		# text_tweet = request.POST['tweet']
		# pub_date = datetime.now()
		# print(request.user)
		# p = Profile.objects.get(user=request.user)
		# t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
		# t.save()
		return redirect('index')
	else:
		return redirect('index')
