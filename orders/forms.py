from django.forms import Form, ModelForm
from orders.models import OrderProduct

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']  
