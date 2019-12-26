from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

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


def LogoutView(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect('home:home')


def SignUpView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, "Succesfully registered")
            return redirect('posts:list')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)












































