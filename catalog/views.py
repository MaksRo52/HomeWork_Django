from django.shortcuts import render
from django.views import generic

from catalog.models import Product


class ProductListView(generic.ListView):
    model = Product


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(generic.DetailView):
    model = Product

