from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador para convertir objetos Product a JSON y viceversa.

    Objetivo:
        Proporcionar una forma de convertir los datos del modelo Product
        a formato JSON para la API REST (/api/), permitiendo que otros
        sistemas o aplicaciones móviles consuman los datos de productos.

        Por ejemplo, si un app móvil hace GET /api/, recibirá un JSON
        con todos los productos disponibles.
    """

    class Meta:
        # Vinculado al modelo Product
        model = Product
        # Campos que se incluirán en la respuesta JSON
        fields = ["name", "price", "description", "available", "photo"]
