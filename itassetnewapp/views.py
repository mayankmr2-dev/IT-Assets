from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import extendeduser, Asset
from .forms import AssetSearchForm, AssetForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def asset_entry(request):
    if request.user:
        title = 'Add Asset'
        form = AssetForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('asset_list')
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'asset_entry.html', context)


@login_required(login_url='/login')
def asset_list(request):
    log_user = request.user
    title = "List of all Assets"
    queryset = Asset.objects.filter(user=log_user)
    form = AssetSearchForm(request.POST or None)

    context = {
        'title': title,
        'queryset': queryset,
        'form': form

    }
    if request.method == 'POST':

        queryset = Asset.objects.all().order_by('-timestamp').filter(

            hostname__icontains=form['hostname'].value(), hosting_location__icontains=form['hosting_location'].value())

        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }

    return render(request, 'asset_list.html', context)


def login(request):
    if request.method == 'POST':
        # check if the user exists
        # with the username and password
        username = request.POST['username']
        user = auth.authenticate(
            username=username, password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            messages.info(request, f"{username}")
            return redirect('asset_list')
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


def logout(request):
    auth.logout(request)
    return redirect('login')
