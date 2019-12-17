from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def posts_create(request):
    return HttpResponse("<h1>Create</h1>")
def posts_detail(request):
    return HttpResponse("<h1>detail</h1>")
def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'posts/index.html', context)
def posts_update(request):
    return HttpResponse("<h1>update</h1>")
def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")

