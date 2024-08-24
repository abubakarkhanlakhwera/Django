from django.shortcuts import render
from .models import Member
def home(req):
    all_members = Member.objects.all
    return render(req, 'home.html', {'all':all_members})