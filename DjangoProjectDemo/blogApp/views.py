from django.shortcuts import render,redirect
from django.contrib import messages

def index(req):
    String='Hello'
    
    return render(req,'blogApp/index.html')
