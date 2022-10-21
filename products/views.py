from django.shortcuts import render, get_object_or_404,  redirect
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


def product_detail(request, category_slug, product_slug):
    """
    View to render the product detail page
    """
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'products/product_detail.html', context)
