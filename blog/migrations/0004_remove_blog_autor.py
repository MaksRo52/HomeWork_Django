# Generated by Django 4.2 on 2024-09-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blog_autor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="autor",
        ),
    ]
