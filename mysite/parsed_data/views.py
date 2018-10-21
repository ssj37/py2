from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getprice(request):
    return render(request, 'stock/getprice.html')

def price(request):
    return render(request, 'stock/price.json')