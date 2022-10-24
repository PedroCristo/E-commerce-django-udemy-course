from django.shortcuts import render, get_object_or_404,  redirect
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
        products = Product.objects.all().filter(
            is_available=True).order_by('id')
        products_count = products.count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
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
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'products/product_detail.html', context)
