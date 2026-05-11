from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderProductForm
from .models import Order, OrderProduct
from products.models import Product


class MiOrdenView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/mi_orden.html'
    context_object_name = 'orden'
    login_url = '/usuarios/login/'  # Redirige acá si no está logueado

    def get_object(self, queryset=None):
        return Order.objects.filter(
            is_active=True,
            user=self.request.user  # Solo la orden del usuario logueado
        ).first()

    def get(self, request, *args, **kwargs):
        orden = self.get_object()
        
        # Si no tiene ninguna orden activa, mostramos un mensaje
        if orden is None:
            return render(request, self.template_name, {'orden': None})
        
        return super().get(request, *args, **kwargs)


def index(request):
    return HttpResponse("Página de órdenes funcionando")


class CreateOrderProductView(LoginRequiredMixin, View):
    login_url = '/usuarios/login/'

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, id=product_id)
        
        # Obtener o crear la orden activa del usuario
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=request.user
        )
        
        # Verificar si el producto ya existe en la orden
        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            product=product,
            defaults={'quantity': 1}
        )
        
        # Si ya existe, incrementar la cantidad
        if not created:
            order_product.quantity += 1
            order_product.save()
        
        return redirect('my_order')