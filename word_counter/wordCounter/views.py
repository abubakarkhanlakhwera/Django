from django.shortcuts import render
from django.http import HttpResponse as hres
# Create your views here.
def index(req):
    return render(req, 'index.html' )

def counter(req):
    words = req.GET['text']
    amount_of_words = len(words.split())
    return render(req,'counter.html' , {'amount': amount_of_words})

# Create your views here.