from django.forms import Form, ModelForm
from orders.models import OrderProduct


class OrderProductForm(ModelForm):
    """
    Formulario para crear/editar productos dentro de una orden.

    Objetivo:
        Proporciona campos para que el usuario seleccione:
        - product: Qué producto quiere agregar
        - quantity: Cuántas unidades quiere

    Aunque no se usa actualmente en la aplicación (los productos se agregan
    automáticamente con cantidad 1), puede usarse en el futuro para permitir
    que el usuario especifique cantidad al agregar.
    """

    class Meta:
        model = OrderProduct
        # Campos que se mostrarán en el formulario
        fields = ["product", "quantity"]
