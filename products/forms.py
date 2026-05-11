from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'photo']
        labels = {
            'name': 'nombre',
            'description': 'descripcion',
            'price': 'precio',
            'available': 'disponible',
            'photo': 'foto',
        }
