from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_info.html', context)
