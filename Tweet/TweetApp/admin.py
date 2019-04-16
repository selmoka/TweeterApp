from django.contrib import admin
from .models import Comment, Tweet, TweetLike

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(TweetLike)