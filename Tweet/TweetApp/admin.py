from django.contrib import admin
from .models import Comment, Tweet

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Comment)