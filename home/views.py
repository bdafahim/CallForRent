from django.shortcuts import redirect, render, HttpResponse

def homeView(request):
    return render(request, 'home/homepage.html')
