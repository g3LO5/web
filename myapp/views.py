<<<<<<< HEAD
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
=======
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
>>>>>>> Naolia_v3

# Create your views here.
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

<<<<<<< HEAD
=======
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
>>>>>>> Naolia_v3

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
