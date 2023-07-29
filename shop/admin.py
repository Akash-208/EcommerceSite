from django.contrib import admin

# Register your models here.
from . models import Product,Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'category','price']

class CartAdmin(admin.ModelAdmin):
    list_display = ['Cprod_id', 'Cprod_name', 'Cprice']


admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
