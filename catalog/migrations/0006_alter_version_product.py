# Generated by Django 5.1.1 on 2024-09-23 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_version_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]
