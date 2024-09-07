
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User

def register(req):
    form = forms.RegisterForm(req.POST)
    if req.method == 'POST':
        
       
        if form.is_valid():
            email_user = form.cleaned_data['email'] 
            emial_query = User.objects.filter(email=email_user).first()
            if emial_query:
                messages.warning(req,"Invalid Email, Try again with a different one")
                return redirect('/auth/register')
            else:
                form.save()
                messages.success(req, 'You have been registered to our website')
              
               
        else:
            messages.warning(req,f'Your form has errors: \n{form.errors}')
            return redirect('/auth/register')
        
    else:
        return render(req, 'blogAuthApp/register.html', {'form': form})

    

