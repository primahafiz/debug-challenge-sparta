from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def signinView(request):
    if (request.user.is_authenticated):
        return redirect('/')
    else:
        if(request.method=='POST'):
            username_login=request.POST['username']
            password_login=request.POST['password']

            user=authenticate(request,username=username_login,password=password_login)

            if (user is not None):
                login(request,user)
                return redirect('/')
            else:
                return redirect('/signin')
    return render(request,'loginPage.html')
