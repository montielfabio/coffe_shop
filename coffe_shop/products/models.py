from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    description = models.TextField(verbose_name="description")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name="foto")


    def __str__(self):
        return self.name

#class listProducts(models.Model):
    name = models.TextField(max_length=200, verbose_name="name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    description = models.TextField(verbose_name="description")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.name