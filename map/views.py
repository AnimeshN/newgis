from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, PassChangeForm
from django.contrib.auth import update_session_auth_hash

# Upload Data
from .forms import LayersForm
from .models import Layers






def home(request):
	return render(request,'map/home.html',{})


def front(request):
	return render(request,'map/front.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='iit').exists():
                login(request, user)
                return redirect('home')
            elif user.groups.filter(name='makerghat').exists():
                login(request, user)
                messages.success(request,('successfully loged in'))
                return redirect('home')
            elif user.groups.filter(name='health').exists():
                login(request, user)
                messages.success(request,('successfully loged in'))
                return redirect('home')
            elif user.groups.filter(name='restricted').exists():
                login(request, user)
                messages.success(request,('successfully loged in'))
                return redirect('home')
            elif user.groups.filter(name='census').exists():
                login(request, user)
                messages.success(request,('successfully loged in'))
                return redirect('home')
            else:
                return HttpResponse("no user groups exist")
        else:
            messages.success(request,('Please try again!'))
            return redirect('login')
    else:
        return render(request,'map/login.html',{})




# def signup_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'map/signup.html', {'form': form})


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'map/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request,('logged out!!'))
    return render(request,'map/login.html',{})

def change_password(request):
    if request.method == 'POST':
        form = PassChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Your password is successfully updated!')
            return redirect('home')
    else:
        form = PassChangeForm(user = request.user) 
    return render(request,'map/changepassword.html',{'form': form})


def demo(request):
    return render(request,'map/demo.html')

def census(request):
    return render(request,'map/census.html',{})    

def iitBombay(request):
    return render(request,'map/iit.html',{})    

def solidWasteManagement(request):
    return render(request,'map/solidwastemanagement.html')

def education(request):
    return render(request,'map/education.html')

def test(request):
    if request.method == 'POST':
        FORM = lA
    return render(request,'map/test.html')    


def health(request):
    return render(request,'map/health.html')

def water(request):
    return render(request,'map/ruralwater.html')

def upload_layers(request):
    if request.method == 'POST':
        form = LayersForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            messages.success(request, 'your file is saved on server')
            return redirect('upload_layers')
    else:
        form = LayersForm()
    return render(request,'map/upload_layers.html',{'form':form})

