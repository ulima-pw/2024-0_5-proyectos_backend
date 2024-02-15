from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Equipo(models.Model):
    EQUIPO_ESTADOS = (
        ("A", "Activo"),
        ("I", "Inactivo")
    )

    nombre = models.CharField(max_length=50)
    anho = models.IntegerField(verbose_name="año", null=True)
    estado = models.CharField(max_length=1, choices=EQUIPO_ESTADOS)

    def __str__(self):
        return self.nombre

class Integrante(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    