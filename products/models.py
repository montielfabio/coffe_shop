from django.db import models


class Product(models.Model):
    """
    Modelo que representa un producto en la cafetería.

    Atributos:
        - name: Nombre del producto (ej: "Café Expreso", "Cappuccino")
        - price: Precio del producto en formato decimal (ej: 2.50)
        - description: Descripción detallada del producto (ingredientes, tamaño, etc)
        - available: Indicador booleano de disponibilidad (True/False)
        - photo: Imagen/foto del producto para mostrar en el catálogo

    Objetivo:
        Almacenar información de todos los productos disponibles en la cafetería
        para que sean mostrados a los clientes en la página principal.
    """

    name = models.CharField(max_length=200, verbose_name="name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    description = models.TextField(verbose_name="description")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )

    def __str__(self):
        """
        Método especial que devuelve el nombre del producto como representación en texto.
        Se utiliza en el admin de Django y en strings del sistema.
        """
        return self.name
