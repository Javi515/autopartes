from django.db import models

class Order(models.Model):
    autopart = models.CharField(max_length=100)
    autopart_url = models.SlugField(max_length=160)
    price = models.PositiveIntegerField("Precio", default=0, help_text="Ingresa el monto en pesos")
    count = models.PositiveSmallIntegerField("Cantidad", default=0)
    description = models.TextField("Descripción", blank=True)
    user_id = models.IntegerField(blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
