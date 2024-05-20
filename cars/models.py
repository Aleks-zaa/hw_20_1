from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категоряия', help_text='Введите категорию')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')
    photo = models.ImageField(upload_to='cars/media', blank=True, null=True, verbose_name='Изображение',
                              help_text='Вставьте Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', help_text='Введите '
                                                                                                          'категорию',
                                 blank=True, null=True, related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену за покупку', blank=True,
                                null=True)
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'created_at', 'updated_at']

    def __str__(self):
        return self.name
