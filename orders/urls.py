from django.urls import path
from .views import CreateOrderProductView, MiOrdenView, index

urlpatterns = [
    path("", index, name="orders_index"),
    path("mi-orden/", MiOrdenView.as_view(), name="my_order"),
    path("agregar-producto/", CreateOrderProductView.as_view(), name="add_product"),
]
