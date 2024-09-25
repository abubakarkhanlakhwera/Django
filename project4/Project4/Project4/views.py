from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req,'website/index.html')
def about(req):
    return HttpResponse("Hello from About.")
def contact(req):
    return HttpResponse("Hello from contact")