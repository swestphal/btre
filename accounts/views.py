from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already used')
                    return redirect('register')
                else:
                    # Everything fine
                    user = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                        email=email
                    )
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do no match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
