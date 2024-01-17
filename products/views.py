from django.shortcuts import render
from django.db.models import Q, F, Count, Avg, Value

from .models import Product, Order, OrderItem



def show_data(requests):
    queryset = OrderItem.objects.annotate(
        total=F('quantity') * F('price')
        ).all()
    
    print(queryset)

        
    return render(requests, 'hello.html', {'orders': list(queryset)})
