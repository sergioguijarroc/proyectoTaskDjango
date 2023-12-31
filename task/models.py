from django.db import models


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


# Create your models here.
