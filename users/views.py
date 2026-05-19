from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    """
    Vista basada en clases para el registro de nuevos usuarios.

    Objetivo:
        Proporcionar un formulario donde los nuevos clientes pueden
        registrarse creando una cuenta con:
        - Username (nombre de usuario)
        - Password (contraseña)
        - Password confirmation (confirmar contraseña)

    Flujo:
        1. Usuario accede a /usuarios/registro/
        2. Ve el formulario de registro (registro.html)
        3. Completa los campos
        4. Django valida que las contraseñas coincidan
        5. Crea la cuenta y lo redirige a /usuarios/login/

    Attributes:
        - form_class: UserCreationForm - Formulario incluido en Django para registro
        - template_name: Archivo HTML donde se muestra el formulario
        - success_url: URL a donde se redirige después del registro exitoso
    """

    # Formulario de creación de usuario de Django (con validación de contraseña)
    form_class = UserCreationForm
    # Plantilla HTML que muestra el formulario de registro
    template_name = "users/registro.html"
    # URL a la que se redirige después del registro exitoso
    success_url = reverse_lazy("login")
