"""
Vistas para la app 'orders' (órdenes/pedidos).

Estas vistas manejan:
- Mostrar el pedido actual del usuario (MiOrdenView)
- Agregar productos al pedido (CreateOrderProductView)
- Página de índice de órdenes (index)

"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderProductForm
from .models import Order, OrderProduct
from products.models import Product


class MiOrdenView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar el pedido actual (activo) del usuario autenticado.

    Objetivo:
        Mostrar una tabla con todos los productos que el usuario ha agregado
        a su pedido actual, permitiéndole revisar antes de confirmar.

    Flujo:
        1. Usuario hace click en "Mi Pedido"
        2. Sistema obtiene su orden activa (is_active=True)
        3. Muestra tabla con productos, cantidades y precios
        4. Usuario puede "Seguir comprando" o "Confirmar pedido"

    LoginRequiredMixin: Requiere que el usuario esté autenticado
    """

    model = Order
    template_name = "orders/mi_orden.html"
    context_object_name = "orden"  # Nombre de la variable en HTML
    login_url = "/usuarios/login/"  # Redirige aquí si no está logueado

    def get_object(self, queryset=None):
        """
        Obtiene la orden activa del usuario actual.

        Objetivo:
            Buscar en BD la orden que tenga:
            - is_active = True (en construcción)
            - user = usuario actual logueado

            Si no existe, retorna None (no hay orden activa aún)

        Retorna:
            Order object o None
        """
        return Order.objects.filter(
            is_active=True, user=self.request.user  # Solo la orden del usuario logueado
        ).first()

    def get(self, request, *args, **kwargs):
        """
        Maneja GET requests a /ordenes/mi-orden/

        Objetivo:
            Mostrar la orden actual del usuario.
            Si no tiene orden activa, muestra un mensaje amigable.

        Retorna:
            Template HTML con los datos de la orden
        """
        orden = self.get_object()

        # Si el usuario no tiene una orden activa aún
        if orden is None:
            return render(request, self.template_name, {"orden": None})

        # Si sí tiene orden, muestra los detalles
        return super().get(request, *args, **kwargs)


def index(request):
    """
    Vista simple para la página de índice de órdenes.

    Objetivo:
        Función placeholder que muestra un mensaje de bienvenida.
        Puede ampliarse en el futuro para mostrar histórico de órdenes,
        órdenes pendientes, etc.

    Retorna:
        HttpResponse con mensaje simple
    """
    return HttpResponse("Página de órdenes funcionando")


class CreateOrderProductView(LoginRequiredMixin, View):
    """
    Vista para agregar un producto a la orden actual del usuario.

    Objetivo:
        Manejar el POST cuando el usuario hace click en "Agregar al pedido".

        El proceso:
        1. Usuario selecciona un producto en la página de catálogo
        2. Hace click en "Agregar al pedido" (submit del formulario)
        3. Se envía POST a /ordenes/agregar-producto/ con product_id
        4. Esta vista:
           a. Obtiene o crea una Order activa para el usuario
           b. Busca si el producto ya está en la orden
           c. Si está: incrementa la cantidad
           d. Si no está: crea nuevo OrderProduct
        5. Redirige a /ordenes/mi-orden/ para ver la orden actualizada

    LoginRequiredMixin: Solo usuarios autenticados pueden agregar al pedido
    """

    login_url = "/usuarios/login/"

    def post(self, request, *args, **kwargs):
        """
        Maneja POST requests para agregar producto a la orden.

        POST data esperado:
            - product: ID del producto a agregar

        Lógica:
            1. Obtiene el ID del producto del formulario
            2. Busca el producto en la BD
            3. Obtiene o crea orden activa para el usuario
            4. Agrega el producto a la orden (o incrementa cantidad)
            5. Redirige a ver la orden actualizada
        """
        # Obtiene el ID del producto del formulario POST
        product_id = request.POST.get("product")
        # Busca el producto, si no existe lanza 404
        product = get_object_or_404(Product, id=product_id)

        # Obtiene o crea la orden activa del usuario
        # get_or_create retorna tupla: (objeto, booleano_si_fue_creado)
        order, _ = Order.objects.get_or_create(is_active=True, user=request.user)

        # Verifica si el producto ya existe en la orden
        order_product, created = OrderProduct.objects.get_or_create(
            order=order, product=product, defaults={"quantity": 1}
        )

        # Si ya existe, incrementar la cantidad
        # Si es nuevo (created=True), deja la cantidad en 1
        if not created:
            order_product.quantity += 1
            order_product.save()

        # Redirige a la página de "Mi Pedido" para ver la orden actualizada
        return redirect("my_order")
