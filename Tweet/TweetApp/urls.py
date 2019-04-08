from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('TweetApp/signup', views.signup, name='signup'),
    path('TweetApp/signin', views.signin, name='signin'),
    # path('herald/articledetail/<int:article_id>', views.articledetail, name='articledetail'),
    # path('herald/authordetail/<int:author_id>', views.authordetail, name='authordetail'),
    # path('herald/signup', views.signup, name='signup'),
]