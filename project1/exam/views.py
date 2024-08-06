from django.shortcuts import render
from django.http import HttpResponse as hres
from django.template import loader

def testpaper(req):
    template = loader.get_template("testpaper.html")
    res = template.render()
    return hres(res)

def result(req):
    template = loader.get_template("testpaper.html")
    res = template.render()
    return hres(res)