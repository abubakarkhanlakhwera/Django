from django.shortcuts import render
from django.http import HttpResponse as hres
from .models import Feature
# Create your views here.
def index(req):
    
    
    return render(req, 'index.html',{'features':features} )

def counter(req):
    words = req.GET['text']
    amount_of_words = len(words.split())
    return render(req,'counter.html' , {'amount': amount_of_words})