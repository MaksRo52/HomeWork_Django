from catalog.models import Product, Category
import json
from django.core.management import BaseCommand


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():  # Здесь мы получаем данные из фикстур с категориями
        with open("catalog/fixture/Catalog_data.json", "r", encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value["model"] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products():  # Здесь мы получаем данные из фикстур с продуктами

        with open("catalog/fixture/Catalog_data.json", "r", encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value["model"] == "catalog.product"]
        return categories

    def handle(self, *args, **options):
        Product.objects.all().delete()  # Удалите все продукты
        Category.objects.all().delete()  # Удалите все категории
        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []
        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    **{
                        "id": category["pk"],
                        "name": category["fields"]["name"],
                        "description": category["fields"]["description"],
                    }
                )
            )
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    **{
                        "id": product["pk"],
                        "name": product["fields"]["name"],
                        "description": product["fields"]["description"],
                        "price": product["fields"]["price"],
                        "category": Category.objects.get(
                            pk=product["fields"]["category"]
                        ),
                        "image": product["fields"]["image"],
                        "created_at": product["fields"]["created_at"],
                        "updated_at": product["fields"]["updated_at"],
                    }
                )
            )
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
