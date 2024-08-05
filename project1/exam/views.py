from django.shortcuts import render
from django.http import HttpResponse as hres

def testpaper(req):
    s="<h1>This is a test paper</h1>"
    return hres(s)

def result(req):
    s="<h1>This your test result</h1>"
    return hres(s)