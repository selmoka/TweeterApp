from django.urls import path, reverse

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('ProfileApp/profile', views.profile, name='profile'),
    path('ProfileApp/addprofile', views.addprofile, name='addprofile'),
]