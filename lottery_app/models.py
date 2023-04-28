from django.db import models


class Sorteo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_sorteo = models.DateField()
    premio = models.CharField(max_length=200)
    sorteo_realizado = models.BooleanField(default=False)

    def __str__(self) -> str:
            return self.nombre

class Participante(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=200, null=True,blank=True)
    nickname = models.CharField(max_length=30, null=True,blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    sorteo = models.ForeignKey("Sorteo", on_delete=models.CASCADE)
    ganador = models.BooleanField(default=False)
    nacionalidad = models.ForeignKey("Nacionalidad", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.pais
