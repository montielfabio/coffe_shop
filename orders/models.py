from django.db import models
from products.models import Product 


#clase Order y OrderProduct para manejar las ordenes y los productos dentro de cada orden
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

#clase OrderProduct para manejar los productos dentro de cada orden, con su cantidad y precio
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order {self.order.id}" 