"""
Configuraciones de URLs principales del proyecto Coffee Shop.

Esta es la configuración central de enrutamiento que dirige las solicitudes
HTTP a las diferentes apps (products, orders, users).

Mapeo de rutas principales:
- /                     -> Redirección a /productos/
- /productos/           -> App products (mostrar catálogo)
- /admin/               -> Panel de administración Django
- /usuarios/            -> App users (login, logout, registro)
- /ordenes/             -> App orders (ver pedidos)

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Redirección de raíz a /productos/
    path("", RedirectView.as_view(url="/productos/", permanent=False)),
    # Incluye todas las URLs de products en /productos/
    path("productos/", include("products.urls")),
    # Panel de administración de Django
    # Accesible en /admin/ (solo para superusuarios)
    path("admin/", admin.site.urls),
    # URLs relacionadas con usuarios (login, logout, registro)
    # Accesibles en /usuarios/
    path("usuarios/", include("users.urls")),
    # URLs relacionadas con órdenes (ver pedidos, agregar productos)
    # Accesibles en /ordenes/
    path("ordenes/", include("orders.urls")),
]

# En modo DEBUG (desarrollo), también servir archivos estáticos y media
if settings.DEBUG:
    # Sirve imágenes subidas por usuarios (fotos de productos)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Sirve archivos estáticos (CSS, JS, imágenes locales)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
