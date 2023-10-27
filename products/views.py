from django.http import HttpResponse
from django.shortcuts import render

from .models import Product



def show_data(requests):
    queryset = Product.objects.filter(id=5)
    product = queryset.first()
    print(product.id)
    print(product.name)
    print(product.price)
        
    return render(requests, 'hello.html')