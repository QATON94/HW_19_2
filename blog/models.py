from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Slug')
    contents = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(blank=True, null=True, verbose_name='превью', upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    publication_sign = models.BooleanField(verbose_name='признак публикации', default=False)
    numbers_views = models.IntegerField(verbose_name='количество просмотров', default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title', 'created_at']
