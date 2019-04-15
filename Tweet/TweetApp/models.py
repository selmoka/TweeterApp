from django.db import models
from django.contrib.auth.models import User
from ProfileApp.models import Profile

class Tweet(models.Model):
	text_tweet = models.CharField(max_length=40)
	pub_date = models.DateTimeField('date published', default=None)
	profile_tweet = models.ForeignKey(Profile, on_delete=models.CASCADE)
	def __str__(self):
		return self.text_tweet

class Comment(models.Model):
	text_comment = models.CharField(max_length=40)
	pub_date = models.DateTimeField('date published', default=None)
	quant_likes = models.IntegerField(default=0)
	tweet_comment = models.ForeignKey(Tweet, on_delete=models.CASCADE, default=None)
	profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
	def __str__(self):
		return self.text_comment