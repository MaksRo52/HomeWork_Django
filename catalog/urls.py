from django.conf import settings
from django.conf.urls.static import static

from catalog.apps import CatalogConfig
from django.urls import path, include
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, CategoryCreateView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_info'),
    path('cr_cat/', CategoryCreateView.as_view(), name='category'),
]
