from django.shortcuts import render

from .models import Auto

def cars_list(request):
    cars = Auto.objects.all()
    return render(request, 'aw_product/cars_list.html', {'cars': cars})