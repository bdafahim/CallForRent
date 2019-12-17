from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_create(request):
    return HttpResponse("<h1>Create</h1>")
def posts_detail(request,id=None):
    #instance = Post.objects.get(id=5)
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'posts/post_detail.html', context)
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

