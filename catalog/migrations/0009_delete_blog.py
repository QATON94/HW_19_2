# Generated by Django 5.0.4 on 2024-04-10 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_blog_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
