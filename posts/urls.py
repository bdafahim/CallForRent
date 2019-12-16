from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('posts/', views.posts_home, name='signout')
]