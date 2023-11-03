from django.db import models
from django.db import models
from django.utils import timezone


class Task(models.Model):
    Nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
