from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register((Category, SubCategory, Review))

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
