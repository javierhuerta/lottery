from django.db import models


class Sorteo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_sorteo = models.DateField()
    premio = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre
    