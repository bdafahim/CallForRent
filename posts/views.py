from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    # if request.method == "POST":
    #     print(request.POST)
    context = {
        "form": form,
    }
    return render(request, 'posts/post_form.html', context)
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

