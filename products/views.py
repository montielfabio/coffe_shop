"""
Vistas para la app 'products' (productos).

Estas vistas manejan:
- Mostrar el catálogo de productos (ProductListView)
- Agregar nuevos productos (ProductFormView)
- Retornar productos en formato JSON para la API (ProductListAPIView)

"""

from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic
from .models import Product
from .forms import ProductForm
from .serializer import ProductSerializer


class ProductFormView(generic.FormView):
    """
    Vista para agregar nuevos productos al catálogo.

    Objetivo:
        Proporciona un formulario HTML para que los gerentes/admin
        agreguen nuevos productos a la cafetería.

    Flujo:
        1. GET /productos/agregar/ -> Muestra formulario vacío
        2. Usuario completa los datos (nombre, precio, foto, etc)
        3. POST con datos -> Django valida
        4. Si es válido, guarda en BD y redirige a este mismo formulario

    Atributos:
        - template_name: Archivo HTML con el formulario
        - form_class: ProductForm (formulario del modelo)
        - success_url: Página a la que ir después de agregar
    """

    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        """
        Método llamado cuando el formulario es válido.

        Objetivo:
            Guardar el nuevo producto en la base de datos.

        Retorna:
            Redirige a success_url (formulario de agregar nuevamente)
        """
        form.save()  # Guarda el producto en la BD
        return super().form_valid(form)


class ProductListView(generic.ListView):
    """
    Vista para mostrar el catálogo de productos (página principal/HOME).

    Objetivo:
        Mostrar a todos los usuarios (autenticados o no) la lista de
        productos disponibles en la cafetería.

    Flujo:
        1. GET / -> Se ejecuta esta vista
        2. Obtiene todos los productos de la BD
        3. Los pasa a la plantilla list_products.html
        4. Muestra tarjetas con fotos, nombres y precios

    Atributos:
        - model: Product (modelo del que obtener datos)
        - template_name: Archivo HTML donde mostrar
        - context_object_name: Nombre de la variable en el HTML ('products')
    """

    model = Product
    template_name = "products/list_products.html"
    context_object_name = "products"


class ProductListAPIView(APIView):
    """
    Vista API para retornar productos en formato JSON.

    Objetivo:
        Proporcionar los datos de productos en formato JSON para que
        otras aplicaciones (móvil, frontend externo, etc) consuman los datos.

    Ejemplo de respuesta:
        GET /api/
        [
          {"name": "Café Expreso", "price": "2.50", ...},
          {"name": "Cappuccino", "price": "3.50", ...}
        ]

    Atributos:
        - authentication_classes: [] (sin autenticación requerida)
        - permission_classes: [] (acceso público)
    """

    # Sin autenticación: cualquiera puede acceder
    authentication_classes = []
    # Sin restricciones de permisos: acceso público
    permission_classes = []

    def get(self, request):
        """
        Maneja GET requests a /api/

        Objetivo:
            Obtener todos los productos y retornarlos como JSON.

        Retorna:
            Response con lista de productos en JSON
        """
        # Obtiene todos los productos de la BD
        products = Product.objects.all()
        # Convierte a JSON usando ProductSerializer
        serializer = ProductSerializer(products, many=True)
        # Retorna el JSON
        return Response(serializer.data)
