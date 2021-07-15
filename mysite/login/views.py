from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .models import Sign_in
from .forms import Sign_inForm
from . import services

def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def home(request):
    return render(request, 'home.html')


def register(request):
    model = Sign_in()
    form = Sign_inForm(request.POST,instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    ctx = {
        'form':form
    }
    return render(request, 'register.html',ctx)


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = services.check_user()
        for i in user:
        	print(i)
        	if i['username']==username and i['password']==password:
        		return redirect("home")
    return render(request, 'login.html')

@login_required_decorator
def logout_user(request):
    logout(request)
    return redirect('login')

# class login(TemplateView):
# 	pass
# 	template_name = 'login.html'
