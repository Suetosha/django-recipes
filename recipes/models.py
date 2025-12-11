from django.db import models


class Recipe(models.Model):
    TYPE_CHOICES = [
        ('Breakfast', 'Завтрак'),
        ('Lunch/Dinner', 'Обед/Ужин'),
        ('Dessert', 'Десерт'),
    ]

    name = models.CharField('Название блюда', max_length=200)
    description = models.TextField('Описание блюда', max_length=800)
    recipe = models.TextField('Рецепт блюда', max_length=1500)
    type = models.CharField('Тип блюда', choices=TYPE_CHOICES)
    photo = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


