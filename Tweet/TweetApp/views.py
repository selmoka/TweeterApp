from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse, Http404
# from .models import Article, Author, Visitor, Comment
from datetime import datetime

# Create your views here.
def index(request):
	# vehicles = Vehicle.objects.all()
	# return render(request, 'articles.html',{
	# 	'articles': Article.objects.all().order_by('-pub_date')
	# }) 
	return HttpResponse('My page')

def signup(request):
	# vehicles = Vehicle.objects.all()
	# return render(request, 'articles.html',{
	# 	'articles': Article.objects.all().order_by('-pub_date')
	# }) 
	return HttpResponse('My page')



# Create your views here.
