from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def SignInView(request):
    return render(request, 'authentication/login.html')
