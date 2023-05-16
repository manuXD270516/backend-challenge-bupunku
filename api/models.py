from django.db import models


class RegistroHora(models.Model):
    hora = models.TimeField()
    minutos = models.IntegerField()

    def __str__(self):
        return f"{self.hora}:{self.minutos}"
