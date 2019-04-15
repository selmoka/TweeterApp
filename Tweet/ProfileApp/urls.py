from django.urls import path, reverse

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('ProfileApp/profile', views.profile, name='profile'),
    path('ProfileApp/addprofile', views.addprofile, name='addprofile'),
    path('ProfileApp/signup', views.signup, name='signup'),
    path('ProfileApp/signin', views.signin, name='signin'),
    path('ProfileApp/signou', views.signout, name='signout'),
]