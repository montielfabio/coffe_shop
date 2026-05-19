from django.db import models
from products.models import Product


class Order(models.Model):
    """
    Modelo que representa un pedido de un cliente.

    Un pedido contiene:
    - Un usuario (cliente) que realizó el pedido
    - Un estado (activo/completado)
    - Una fecha de creación
    - Una relación con múltiples productos (a través de OrderProduct)

    Objetivo:
        Almacenar la información de cada pedido realizado por un cliente.
        Cada usuario puede tener múltiples órdenes, pero solo UNA orden activa
        (en construcción) a la vez. Una vez completada, se marca como inactiva.

    Flujo:
        1. Usuario agrega un producto al pedido
        2. Se crea una Order activa (is_active=True)
        3. Se agregan OrderProducts a esta Order
        4. Usuario puede ver su pedido en "Mi Pedido"
        5. Cuando confirma, se marca como inactiva
    """

    # ForeignKey al modelo User de Django
    # Si un usuario se elimina, sus órdenes también se eliminarán (CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    # Booleano para saber si la orden está en construcción (True) o completada (False)
    # Por defecto es True (nueva orden)
    is_active = models.BooleanField(default=True)

    # Fecha y hora de creación del pedido
    # auto_now_add=True significa que se asigna automáticamente a la fecha actual
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Representación en texto del pedido.
        Ejemplo: "Order 5 by juan_perez"
        """
        return f"Order {self.id} by {self.user.username}"


class OrderProduct(models.Model):
    """
    Modelo que representa UN producto dentro de un pedido.

    Objetivo:
        Actúa como tabla intermedia (muchos-a-muchos) entre Order y Product.
        Almacena:
        - Qué pedido contiene el producto
        - Cuál es el producto
        - Cuántas unidades del producto se solicitaron

    Ejemplo:
        Order #5 puede tener 3 OrderProducts:
        - 2x Café Expreso
        - 1x Cappuccino
        - 1x Croissant
    """

    # ForeignKey a Order
    # related_name='order_products' permite acceder a los productos de una orden
    # con: orden.order_products.all()
    # CASCADE: si se elimina la orden, se eliminan sus productos también
    order = models.ForeignKey(
        Order, related_name="order_products", on_delete=models.CASCADE
    )

    # ForeignKey a Product
    # PROTECT: previene eliminar un producto si está en una orden
    # (No se puede eliminar un producto del catálogo si ya fue pedido)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    # Cantidad de unidades de este producto en la orden
    # Ej: si el usuario agrega dos cafés, quantity=2
    quantity = models.PositiveIntegerField()

    def __str__(self):
        """
        Representación en texto del producto en una orden.
        Ejemplo: "2 x Café Expreso for Order 5"
        """
        return f"{self.quantity} x {self.product.name} for Order {self.order.id}"
