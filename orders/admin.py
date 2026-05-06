from django.contrib import admin
from .models import Order, OrderProduct

#esta clase permite mostrar los productos dentro de cada orden en el admin de Django, con su cantidad y precio
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

# en esta clase se registra el modelo Order en el admin de Django, y se incluye la clase OrderProductInlineAdmin para mostrar los productos dentro de cada orden
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]

admin.site.register(Order, OrderAdmin)  