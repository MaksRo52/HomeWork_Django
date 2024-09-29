# Generated by Django 5.1.1 on 2024-09-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок.",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Введите текст статьи.", verbose_name="Содержание"
                    ),
                ),
                ("slug", models.CharField(blank=True, max_length=100, unique=True)),
                (
                    "image",
                    models.ImageField(
                        help_text="Загрузите изображение статьи.",
                        upload_to="media/",
                        verbose_name="Изображение",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Просмотры")),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ["-created_at", "-status"],
            },
        ),
    ]
