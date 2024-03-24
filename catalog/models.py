from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='описание')
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey("Category", on_delete = models.CASCADE)
    price_for_purchase = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
