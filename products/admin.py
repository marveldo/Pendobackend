from django.contrib import admin
from .models import Products
# Register your models here.

class ProductModelClass(admin.ModelAdmin):
    list_display = ['name', 'description' , 'id', 'current_price' ]
admin.site.register(Products, ProductModelClass)

