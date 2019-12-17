from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('list/', views.posts_list, name='list'),
    path('create/', views.posts_create, name='posts'),
    path('detail/', views.posts_detail, name='deteil'),
    path('update/', views.posts_update, name='update'),
    path('delete/', views.posts_delete, name='delete'),

]