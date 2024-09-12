from django.conf import settings
from django.conf.urls.static import static

from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import ProductListView, contacts, product_info

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product_info, name='product_info')
]
