from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField

from .models import *



def show_data(requests):
    queryset = Comment.objects.all()
    
    print(queryset)

        
    return render(requests, 'hello.html', {'orders': list(queryset)})
