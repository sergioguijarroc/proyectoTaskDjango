from django import forms


"""
#De esta forma cogemos los datos del modelo, es la más rápida y cómoda

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["nombre", "descripcion", "realizada"]
"""


class TaskForm(forms.Form):
    nombre = forms.CharField(label="title", max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea, label="descipcion")
    realizada = forms.BooleanField(label="completed", required=False)


# De esta otra forma, validamos los datos a mano en este mismo archivo
