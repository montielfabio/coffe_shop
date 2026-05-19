from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView

"""
Configuraciones de URLs para la app 'users' (usuarios).

Estas rutas manejan:
- Inicio de sesión (login)
- Cierre de sesión (logout)
- Registro de nuevos usuarios

El flujo de usuario:
1. Nuevo usuario: /usuarios/registro/ -> Crear cuenta
2. Usuario existente: /usuarios/login/ -> Iniciar sesión
3. Usuario autenticado: /usuarios/logout/ -> Cerrar sesión

"""

urlpatterns = [
    # Ruta para iniciar sesión
    # Usa la vista LoginView incluida en Django
    # template_name especifica el archivo HTML personalizado
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    # Ruta para cerrar sesión
    # Usa la vista LogoutView incluida en Django
    # Después del logout, redirige a LOGOUT_REDIRECT_URL en settings
    path("logout/", LogoutView.as_view(), name="logout"),
    # Ruta para registrarse como nuevo usuario
    # Usa RegisterView personalizada en views.py
    path("registro/", RegisterView.as_view(), name="registro"),
]
