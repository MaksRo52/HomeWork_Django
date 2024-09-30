from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import (
    ProductListView,
    ContactsView,
    ProductDetailView,
    ProductCreateView,
    CategoryCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_info"),
    path("cr_cat/", CategoryCreateView.as_view(), name="category"),
]
