from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    """
    Administrador en línea (inline) para mostrar productos dentro de una orden.

    Objetivo:
        Permite ver y editar los productos de una orden directamente
        en la página de detalle de la orden (sin ir a otra página).

    Aparece como una tabla dentro de la orden mostrando:
    - Nombre del producto
    - Cantidad
    - Precio

    extra = 0 significa que no muestra filas vacías para agregar nuevos productos
    """

    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """
    Personalización del administrador Django para el modelo Order.

    Objetivo:
        Proporcionar una interfaz en /admin/ para que los gerentes
        puedan:
        - Ver todas las órdenes realizadas
        - Ver qué productos están en cada orden
        - Ver el cliente que realizó cada orden
        - Ver la fecha de cada pedido
        - Editar o eliminar órdenes si es necesario

    El 'inlines' incluye OrderProductInlineAdmin para que los productos
    se muestren directamente en la página de la orden.
    """

    model = Order
    # Muestra OrderProductInlineAdmin dentro de esta página
    inlines = [OrderProductInlineAdmin]


# Registra el modelo Order en el admin con la clase OrderAdmin personalizada
admin.site.register(Order, OrderAdmin)
