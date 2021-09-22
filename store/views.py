from django.shortcuts import get_object_or_404, render
from .models import Genre, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def genre_list(request, genre_slug=None):
    genre = get_object_or_404(Genre, slug=genre_slug)
    products = Product.products.filter(genre=genre)
    return render(request, 'store/genre.html', {'genre': genre, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})
