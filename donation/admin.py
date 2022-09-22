from django.contrib import admin
from .models import Category, Article, Image
# from models import Callback, Collection, Image, Product, Cart, Order, CartItem


class ImageInline(admin.TabularInline):
    model = Image
    max_num = 12
    min_num = 1
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    list_display = ('title', 'categoryId', 'description', 'target', 'progress', 'charityQty', 'city', 'owner',
                    'phone_number', 'creation_date', 'end_date', 'requisites')

