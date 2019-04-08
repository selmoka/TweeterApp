from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length=140, default='')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Tweet(models.Model):
	text = models.CharField(max_length=40)
	profile_tweet = models.ForeignKey(Profile, on_delete=models.CASCADE)
	def __str__(self):
		return self.text

class Comment(models.Model):
	text = models.CharField(max_length=40)
	profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)

