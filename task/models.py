from django.db import models


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}\n{self.descripcion}"


# Create your models here.
