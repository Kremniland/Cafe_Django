from django.db import models

'''"Название", "Объем", "Описание", "Цена", "Рецепт", "Картинка" и также добавив технические 
(те, которым обычным пользователям будут не доступны) "Дата добавления записи", "Дата обновления записи", 
"Логическое существование"'''

class coffe(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    recipe = models.TextField(blank=True, null=True, verbose_name='Рецепт')
    image = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Картинка')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления записи')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления записи')
    exists = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta():
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'
        ordering = ['name']

