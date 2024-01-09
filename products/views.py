from django.shortcuts import render

from .models import Product



def show_data(requests):
    queryset = Product.objects.filter(inventory__lt=5)

        
    return render(requests, 'hello.html', {'products': list(queryset)})
