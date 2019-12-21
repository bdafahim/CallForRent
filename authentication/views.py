from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def SignInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully loged in")
            return redirect('posts:list')

        else:
            messages.success(request, "Wrong Email or password")
            return redirect('authentication:signin')

    else:
        return render(request, 'authentication/login.html')
