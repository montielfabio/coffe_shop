from django.contrib import admin
from .models import Product


#clase para personalizar la forma en que se muestran los productos en el admin de Django
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'available'] #para mostrar el nombre, precio y disponibilidad del producto en la lista de productos en el admin
    search_fields = ['name'] #para buscar por nombre o descripción del producto

admin.site.register(Product, ProductAdmin)
