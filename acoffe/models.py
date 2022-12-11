from django.db import models

from django.urls import reverse


class coffe(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    recipe = models.TextField(blank=True, null=True, verbose_name='Рецепт')
    image = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Картинка')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления записи')
    exists = models.BooleanField(default=True)
    volume = models.IntegerField(default=200, blank=True, verbose_name='Объем')


    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('detail_coffe', kwargs={'coffe_id': self.pk})



class ingridient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Картинка')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления записи')
    exists = models.BooleanField(default=True)
    
    coffe = models.ManyToManyField(coffe, related_name='ingridients')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ['name']
