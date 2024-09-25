import random

from django.shortcuts import render

from django.core.cache import cache
from .models import Category, Banner


def catalog_view(request):
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.filter(is_active=True)
        cache.set('categories', categories, 86400)  # кеш на сутки
    return render(request, 'catalog.html', {'categories': categories})


def home_view(request):
    banners = cache.get('banners')
    if not banners:
        banners = list(Banner.objects.filter(is_active=True))
        banners = random.sample(banners, min(3, len(banners)))
        cache.set('banners', banners, 600)
    return render(request, 'home.html', {'banners': banners})
