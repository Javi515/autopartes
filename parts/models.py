from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Categorías"""
    name = models.CharField("Categoría", max_length=150)
    description = models.TextField("Descripción")
    url = models.SlugField(max_length=160)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Automake(models.Model):
    """Fabricantes de autos"""
    name = models.CharField("Nombre", max_length=150)
    description = models.TextField("Descripción")
    image = models.ImageField("Imagen", upload_to="automakes/", null=True)
    url = models.SlugField(max_length=160)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fabricante de autos"
        verbose_name_plural = "Fabricantes de autos"

class Autopart(models.Model):
    """Autopartes"""
    title = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción")
    image = models.ImageField("Imagen", upload_to="autoparts/")
    automake = models.ManyToManyField(Automake, verbose_name="Fabricante", related_name="autopart_automake")
    count = models.PositiveSmallIntegerField("Cantidad", default=0)
    category = models.ForeignKey(
        Category, verbose_name="Categoría", on_delete=models.SET_NULL, null=True
    )
    price = models.PositiveIntegerField("Precio", default=0, help_text="Ingresa el precio en pesos")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Borrador", default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("autopart_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Autoparte"
        verbose_name_plural = "Autopartes"
