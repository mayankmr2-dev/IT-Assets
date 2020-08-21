from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import extendeduser

# def home(request):
#     return HttpResponse("Wow great job")


def login(request):
    if request.method == 'POST':
        # check if the user exists
        # with the username and password
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # both the passwords matched
            # now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username already exists !"})
            except User.DoesNotExist:
                fullname = request.POST['fullname']
                email = request.POST['email']
                phonenumber = request.POST['phonenumber']
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password'])
                unit = request.POST['unit']
                nenwextendeduser = extendeduser(
                    fullname=fullname, email=email, phonenumber=phonenumber, user=user, unit=unit)
                nenwextendeduser.save()
                auth.login(request, user)
                return HttpResponse("Registered Successfully !")
                # fullname,email,phonenumber,unit
        else:
            return render(request, 'register.html', {'error': "Passwords don't match !"})
    else:
        return render(request, 'register.html')
