from django.shortcuts import render ,redirect
from .models import Post

def index(req):
    posts = Post.objects.all()
    return render(req,'index.html', {'posts':posts})