from django.shortcuts import render ,redirect
from django.http import HttpResponse as hres
from .models import Feature
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib import auth


def index(req):
    feature1 =Feature()
    feature1.name= 'Abubakar'
    feature1.detail = 'Our servic is fast.'
    features = [feature1]
    return render(req,'index.html',{"features":features})

def register(req):
    if req.method == "POST":
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(req,'Email already used.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                    messages.info(req,'Username already used.')  
                    return redirect('register')
            else :
                 user = User.objects.create_user(username=username, email=email, password=password) 
                 user.save()
                 return redirect('register') 
        else:
             messages.info(req,'Password is not same')
             return redirect('register')
                   
    return render(req, 'register.html')

def login(req):
     if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req,'Credentials not found')
            return redirect('login')

     else:     
        return render(req,"login.html")

def post(req,id):
    posts=[1,2,4,'ALi',"Ahmad","Basit"]
    return render(req,'post.html', {'posts':posts})

def counter(req):
    
    posts=[1,2,4,'ALi',"Ahmad","Basit"]
    return render(req,'counter.html',{'posts':posts})

