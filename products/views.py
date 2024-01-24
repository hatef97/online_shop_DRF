from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField

from .models import *



def show_data(requests):
    category = Category(id=100)
    category.title = 'cars'
    category.description = 'New 2023 top cars'
    category.save()
    query = Category.objects.get(id=100)
    
    print(query)

        
    return render(requests, 'hello.html')
