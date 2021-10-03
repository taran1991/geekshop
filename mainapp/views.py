
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, ProductCategory
from basketapp.models import Basket

import random


def get_hot_product():
    products = Product.objects.all()
    return random.choice(products)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    sample_len = 3 if len(same_products) >= 3 else len(same_products)
    print(sample_len)
    same_products = random.sample(list(same_products), sample_len)
    return same_products


def main(request):
    content = {'products': Product.objects.all()[2:4],}
    return render(request, 'mainapp/index.html', content)

def contacts(request):
    content = {
        'contacts':
        [['Москва', 'info@geekshop.ru', '+7-888-888-8888', 'В пределах МКАД'],
        ['Москва', 'info@geekshop.ru', '+7-888-888-8888', 'В пределах МКАД'],
        ['Москва', 'info@geekshop.ru', '+7-888-888-8888', 'В пределах МКАД'],
        ],
    }
    return render(request, 'mainapp/contact.html', content)


def get_paginator(products, page, quantity=2):
    paginator = Paginator(products, quantity)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    return products_paginator


def products(request, pk=None, page=1):
    links = ProductCategory.objects.filter(is_active=True)
    title = 'продукты'

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        content = {
            'title': title,
            'links': links,
            'category': category,
            'products': get_paginator(products, page, 2),
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


    content = {
        'links': links,
        'products': products[:3],
        'title': title,
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)
