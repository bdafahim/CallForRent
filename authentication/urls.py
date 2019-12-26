from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'authentication'

urlpatterns = [
 path('signin/', views.SignInView, name='signin'),
 path('signout/', views.LogoutView, name='signout'),
 path('register/', views.SignUpView, name='register'),
]