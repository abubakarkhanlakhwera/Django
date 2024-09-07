from django.shortcuts import render
from django.contrib import messages

def Home(req):
    string= 'hello'
    messages.warning(req,"This is a flash message")
    return render(req,'blogApp/index.html',{'string':string})

def About(req):
    return render(req,'blogApp/about.html',{})
