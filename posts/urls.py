from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='posts'),
    path('<int:id>/', views.posts_detail, name='detail'),
    path('update/', views.posts_update, name='update'),
    path('delete/', views.posts_delete, name='delete'),

]