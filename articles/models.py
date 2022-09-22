from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    """ Модель для Категории """
    name = models.CharField(max_length=100, verbose_name='Категории')
    description = models.CharField(max_length=150, unique=False, verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):

    """ Модель для Объявлений """

    title = models.CharField(max_length=150, unique=False, verbose_name='Название')
    categoryId = models.ForeignKey(Category,  on_delete=models.CASCADE, blank=True, related_name='articles')
    description = models.CharField(max_length=150, unique=False, verbose_name='Описание')
    target = models.PositiveIntegerField(verbose_name='Нужная сумма')
    progress = models.PositiveIntegerField(verbose_name='Собранные средства')
    charityQty = models.PositiveIntegerField(verbose_name='Спонсоры')
    city = models.CharField(max_length=40, verbose_name='Город')
    owner = models.CharField(max_length=40, verbose_name='ФИО Получателя')
    phone_number = PhoneNumberField(blank=True, null=False, verbose_name="Tелефон")
    creation_date = models.DateField(verbose_name='Дата создания')
    end_date = models.DateField(verbose_name='Дата окончания')
    requisites = models.CharField(max_length=255, verbose_name='Реквизиты')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id", "-creation_date"]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Image(models.Model):
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_images')
    image = models.ImageField(verbose_name='Фотография', null=True, blank=True)


# class Requisites(models.Model):
#     articleId = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_requisites')
#     requisites = models.CharField(max_length=40, verbose_name='Реквизиты', null=True, blank=True)
