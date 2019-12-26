from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.db.models import Q
from .forms import PostForm
from authentication.models import User

def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
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
        "instance": instance,
    }
    return render(request, 'posts/post_detail.html', context)
def posts_list(request):
    user = request.user
    queryset = Post.objects.all() #.order_by("-time_stamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        "object_list": queryset,
        "title": "List",
        'user': user,
    }
    return render(request, 'posts/index.html', context)
def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, 'posts/post_form.html', context)
def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "susccesfully deleted")
    return redirect("posts:list")

