from django.shortcuts import render
from django.db.models import Q, F, Count, Avg

from .models import Product, Order, OrderItem



def show_data(requests):
    queryset = Product.objects.filter(datetime_created__year=2022).aggregate(
        Count('id')
    )
    
    print(queryset)

        
    return render(requests, 'hello.html', {'orders': list(queryset)})
