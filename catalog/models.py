from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text="Введите название.")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание.")
    image = models.ImageField(upload_to='media/',
                              verbose_name='Фото',
                              help_text="Загрузите изображение продукта.",
                              null=True,
                              blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name="Стоимость",
                                blank=True,
                                help_text="Введите цену в рублях.",
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта',
                                           editable=False,
                                           blank=True,
                                           null=True)

    class Meta:
        verbose_name = 'Продукт'

        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at', 'category']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text="Введите название.")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание.")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text="Введите заголовок.")
    content = models.TextField(verbose_name='Содержание', help_text="Введите текст статьи.")
    slug = models.CharField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='media/', verbose_name='Изображение', help_text="Загрузите изображение статьи.")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at', '-status']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
