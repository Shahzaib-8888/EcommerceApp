from django.shortcuts import render

# Create your views here.
from .models import *

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})


def home(request):
    return render(request, 'home.html')
