from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Clase que personaliza la interfaz del administrador Django para el modelo Product.

    Objetivo:
        Proporcionar una interfaz mejorada en /admin/ para que los gerentes
        de la cafetería puedan:
        - Ver la lista de todos los productos disponibles
        - Buscar productos por nombre
        - Agregar, editar y eliminar productos
        - Ver el estado de disponibilidad de cada producto
    """

    model = Product
    # Columnas que se mostrarán en la tabla de productos del admin
    # Esto facilita ver rápidamente el nombre, precio y disponibilidad
    list_display = ["name", "price", "available"]
    # Campos por los que se puede buscar en el admin
    # El usuario puede escribir un nombre y filtrar rápidamente
    search_fields = ["name"]


# Registra el modelo Product en el admin con la clase ProductAdmin personalizada
admin.site.register(Product, ProductAdmin)
