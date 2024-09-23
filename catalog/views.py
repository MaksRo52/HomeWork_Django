from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Category


class ProductListView(generic.ListView):
    model = Product


class ContactsView(generic.TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ["name", "description"]
