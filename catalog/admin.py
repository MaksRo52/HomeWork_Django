from django.contrib import admin
from catalog.models import Product, Category, Version
from users.models import User


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version', 'active')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'token')
