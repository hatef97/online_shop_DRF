from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField

from .models import Product, Order, OrderItem, Customer



def show_data(requests):
    queryset = OrderItem.objects.annotate(
        total_price = ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField()))
    
    print(queryset)

        
    return render(requests, 'hello.html', {'orders': list(queryset)})
