from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from authentication.models import User

def SignInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print(user)
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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email).exists():
                form.add_error("email", 'Email Address Taken')
            else:
                current_user = User.objects.create_user(email=email, password=password)
                user_detail = form.save(commit=False)
                user_detail.user = current_user
                #user_detail.is_active = False
                current_user.save()
                user_detail.save()
                # user = authenticate(request, email=email, password=password)
                login(request, current_user)
                messages.success(request, "Succesfully registered")
                return redirect('posts:list')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)











































