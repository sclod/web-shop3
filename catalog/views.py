from django.shortcuts import render
from .models import Product, Producer, Category
from django.core.paginator import Paginator


def index(request):
    return render(request, 'catalog/index.html', context={
        'all_products': Product.objects.all(),
    })


def create(request):
    return render(request, 'catalog/create.html', context={
        'title': 'Добавление товаров'
    })


def details(request, id):
    return render(request, 'catalog/details.html', context={
        'title': 'Просмотр информации'
    })


def update(request, id):
    return render(request, 'catalog/update.html', context={
        'title': 'Редактирование товаров'
    })


def delete(request, id):
    return render(request, 'catalog/delete.html', context={
        'title': 'Удаление товаров'
    })


