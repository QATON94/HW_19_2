# Generated by Django 5.0.4 on 2024-04-22 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0010_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions',
                                    to='catalog.product', verbose_name='Продукт'),
        ),
    ]
