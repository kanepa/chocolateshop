from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)

    try:

        products = paginator.page(page)

    except PageNotAnInteger:

        products = paginator.page(1)

    except EmptyPage:

        products = paginator.page(paginator.num_pages)

    return render(request, 'products/products.html', {'products': products})




