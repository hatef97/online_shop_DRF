from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField

from .models import *



def show_data(requests):
    queryset = Order.unpaid_manager.all()
    
    print(queryset)

        
    return render(requests, 'hello.html')
