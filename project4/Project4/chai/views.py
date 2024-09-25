from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

def all_chai(req):
    chais = ChaiVariety.objects.all()
    
    return render(req,'chai/chai.html',{'chais':chais})
def chai_detail(req,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(req,'chai/chai_detail.html',{'chai':chai})
def Price(req,price_id):
    price = get_object_or_404(ChaiVariety,pk=price_id)
    return render(req, 'chai/price.html',{'price':price})