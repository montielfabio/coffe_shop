from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Formulario basado en ModelForm para crear y editar productos.

    Objetivo:
        Proporcionar una interfaz en HTML para que el administrador agregue
        nuevos productos al catálogo de la cafetería.

        Django convierte automáticamente los campos del modelo Product en
        campos de formulario HTML (input, textarea, etc).
    """

    class Meta:
        # Se vincula al modelo Product
        model = Product
        # Campos que se mostrarán en el formulario
        fields = ["name", "description", "price", "available", "photo"]
        # Etiquetas personalizadas en español para los campos
        labels = {
            "name": "nombre",
            "description": "descripcion",
            "price": "precio",
            "available": "disponible",
            "photo": "foto",
        }
