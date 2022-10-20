from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def products(request, category_slug=None):
    """
    View to render the products page
    """
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'products/products.html', context)
