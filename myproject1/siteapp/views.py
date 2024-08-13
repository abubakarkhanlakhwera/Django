from django.shortcuts import render
from django.http import HttpResponse as hres

def index(req):
    context = {
        "name": "Abubakar",
        "subject": 'python',
        "age": '29',
        "nationality": 'Pakistani'
    }
    return render(req, 'index.html', context)

# Create your views here.
