from django.shortcuts import render
from .models import Product


def products(request):
    """
    View to render the products page
    """
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'products/products.html', context)

