from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="nombre")
    description = forms.CharField(max_length=300, label="descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="precio")
    available = forms.BooleanField(initial=True, label="disponible")
    photo = forms.ImageField(required=False, label="foto")

    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo']
        )
