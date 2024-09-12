from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


# Create your views here.
# def home(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'products_list.html', context)

class ProductListView(ListView):
    model = Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_info.html', context)
