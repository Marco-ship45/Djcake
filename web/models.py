from django.db import models


class Pastel(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    imagen = models.ImageField(
        upload_to='pasteles/'
    )


    def __str__(self):
        return self.nombre