from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='create'),
    path('<int:id>/', views.posts_detail, name='detail'),
    path('<int:id>/edit/', views.posts_update, name='update'),
    path('<int:id>/delete/', views.posts_delete, name='delete'),

]