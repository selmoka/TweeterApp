from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tweet.settings')

import django
django.setup()

from TweetApp.models import Tweet, Comment
from ProfileApp.models import Profile
from faker import Faker
from django.contrib.auth.models import User

if __name__ == '__main__':
	print('Starting to populate...')
	Tweet.objects.all().delete()
	Comment.objects.all().delete()
	Profile.objects.all().delete()

	fake = Faker()
	for _ in range(1,50):
		username = fake.user_name()
		password = fake.password()
		bio = 'https://picsum.photos/200/300/?random'
		user = User.objects.create_user(username=username, password=password)
		user.save()
		try:
			p = Profile(bio=bio, user=user)
			p.save()

			text_tweet = fake.text()
			pub_date = fake.date()
			t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
			print(t)
			t.save()
		except:
			pass
		
	print('Finished populating!')