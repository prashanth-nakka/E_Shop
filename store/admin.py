from django.contrib import admin
from .models import Product, Category, Customer
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'image', ]
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_filter = ['id', 'name', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
