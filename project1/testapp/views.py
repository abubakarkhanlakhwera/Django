from django.shortcuts import render
from django.http import HttpResponse as hres

def greeting(request):
    s='<h1>Hello and Welcome</h1>'
    return hres(s)

def about(request):
    s="<h1>About page</h1>"
    return hres(s)

def contact(request):
    s="<h1>Contact page</h1>"
    return hres(s)


