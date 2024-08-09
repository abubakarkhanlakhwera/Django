from django.shortcuts import render
from django.http import HttpResponse as hres
from .models import Feature
# Create your views here.
def index(req):
    
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very fast'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is consistently reliable'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Secure'
    feature3.details = 'Our service ensures top-level security'
    feature3.is_true = True

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'User-Friendly'
    feature4.details = 'Our service is designed to be user-friendly'
    feature4.is_true = True

    features = [feature1,feature2,feature3,feature4]
    return render(req, 'index.html',{'features':features} )

def counter(req):
    words = req.GET['text']
    amount_of_words = len(words.split())
    return render(req,'counter.html' , {'amount': amount_of_words})