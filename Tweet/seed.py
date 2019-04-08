from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tweet.settings')

import django
django.setup()

from TweetApp.models import Tweet, Comment, Profile
from faker import Faker
from django.contrib.auth.models import User

if __name__ == '__main__':
	print('Starting to populate...')
    # call your script's functions here
	fake = Faker()
	for _ in range(1,50):
		username = fake.first_name()
		password = fake.password()
		bio = fake.text()
		user = User.objects.create_user(username=username, password=password)
		user.save()

		p = Profile(bio=bio, user=user)
		p.save()

		text_twwet = fake.text()
		pub_date = fake.date()
		t = Tweet(text_tweet=text_tweet, pub_date=pub_date, profile_tweet=p)
		t.save()

		# text = fake.text()
		# pub_date = fake.date()
		# visitor_comment = v
		# article_comment = a
		# c = Comment(comment_text=comment_text, pub_date=pub_date, 
		# 	visitor_comment=visitor_comment, article_comment=article_comment)
		# c.save()
		print('Finished populating!')