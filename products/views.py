from django.shortcuts import render
from django.db.models import Q, F

from .models import Product, Order, OrderItem



def show_data(requests):
    queryset = OrderItem.objects.filter(product_id=F('quantity'))

        
    return render(requests, 'hello.html', {'products': list(queryset)})
