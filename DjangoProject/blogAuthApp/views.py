
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required

def register(req):
    form = forms.RegisterForm(req.POST)
    if req.method == 'POST':
        
       
        if form.is_valid():
            email_user = form.cleaned_data['email'] 
            email_query = User.objects.filter(email=email_user).first()
            if email_query:
                messages.warning(req,"Invalid Email, Try again with a different one")
                return redirect('/auth/register')
            else:
                form.save()
                messages.success(req, 'You have been registered to our website')
                return redirect('/')
              
               
        else:
            messages.warning(req,f'Your form has errors: \n{form.errors}')
            return redirect('/auth/register')
        
    else:
        return render(req, 'blogAuthApp/register.html', {'form': form})

    
def loginUser(req):
    form = forms.LoginForm(req.POST)
    if req.user.is_authenticated:
        messages.warning(req,'You are already logged in!')
        return redirect('/')
    if req.method == 'POST':
        if form.is_valid():
            attempt = authenticate(
                req, 
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if attempt:
                login(req,attempt)   
                messages.success(req,'You are now logged in!') 
                return redirect('/')
            else:
                messages.warning(req,'Invalid username or password')
                return redirect('/auth/login')
                                       
        else:
            messages.warning(req,f'Your form has errors: \n{form.errors}')
            return redirect('/auth/register')     
    else:
        return render(req,'blogAuthApp/login.html',{'form':form})
@login_required(login_url='/auth/login')
def logoutUser(req):
    logout(req)
    messages.success(req,'You are logged out!')
    return redirect('/auth/login')