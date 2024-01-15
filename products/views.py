from django.shortcuts import render
from django.db.models import Q, F

from .models import Product, Order, OrderItem



def show_data(requests):
    queryset = Order.objects.select_related('customer').prefetch_related('items__product').all()

        
    return render(requests, 'hello.html', {'orders': list(queryset)})
