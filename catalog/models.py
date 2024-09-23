from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="Введите название."
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание."
    )
    image = models.ImageField(
        upload_to="media/",
        verbose_name="Фото",
        help_text="Загрузите изображение продукта.",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.IntegerField(
        verbose_name="Стоимость",
        blank=True,
        help_text="Введите цену в рублях.",
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateTimeField(
        verbose_name="Дата производства продукта", editable=False, blank=True, null=True
    )

    class Meta:
        verbose_name = "Продукт"

        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at", "category"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="Введите название."
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание.", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version = models.CharField(
        max_length=100, verbose_name="Версия", help_text="Введите версию продукта."
    )
    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название версии."
    )
    active = models.BooleanField(default=False, verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["product", "version", "active"]

    def __str__(self):
        return f"{self.product.name} - {self.version}"
