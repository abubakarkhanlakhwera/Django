from django.shortcuts import render
from django.http import HttpResponse as hres
from .models import Feature

def index(req):
    feature1 =Feature()
    feature1.name= 'Abubakar'
    feature1.detail = 'Our servic is fast.'
    features = [feature1]
    return render(req,'index.html',{"features":features})

def counter(req):
    words = req.GET['text']
    amount_of_words = len(words.split())
    return render(req,'counter.html', {'amount':amount_of_words})

