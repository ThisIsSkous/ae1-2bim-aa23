from django.db import models

# Create your models here.
class EntidadInventario(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=15)

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                """ % (self.nombre,
                self.siglas,

                