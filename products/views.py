from django.shortcuts import render
from django.db.models import Q, F

from .models import Product, Order, OrderItem



def show_data(requests):
    queryset = Product.objects.prefetch_related('order_items').all()

        
    return render(requests, 'hello.html', {'products': list(queryset)})
