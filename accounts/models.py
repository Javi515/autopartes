from django.db import models

class User_Panel(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=100, null=True, blank=True)
    email = models.CharField("Correo electrónico", max_length=255)
    photo = models.ImageField("Foto de perfil", upload_to='users/', blank=True, default='static/img/default.jpg')
    staff = models.BooleanField("Personal", default=False)
    individual = models.BooleanField("Persona individual", default=True)
    panel_id = models.IntegerField("ID de panel", blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
