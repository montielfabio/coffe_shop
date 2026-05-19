from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPIView

app_name = "products"  # ← agregá esta línea

urlpatterns = [
    path("", ProductListView.as_view(), name="list_products"),
    path("api/", ProductListAPIView.as_view(), name="list_products_api"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
]
