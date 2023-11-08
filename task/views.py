from django.shortcuts import render, redirect
from .models import Task
from .forms import (
    TaskForm,
)  # Hay que importar el formulario que he generado en el archivo forms, TaskForm es la clase


# Create your views here.
def task_list(request):
    tasks = (
        Task.objects.all()
    )  # Esto coge todos los objetos del modelo(la base de datos)

    if (
        request.method == "POST"
    ):  # En el caso que la request venga de que he pulsado el botón enviar del formulario y viene con un POST
        form = TaskForm(request.POST)
        if form.is_valid():  # Si está validado, lo guardamos
            form.save()  # Esto hace que se guarde en la base de datos
            return redirect(
                "task_list"
            )  # Hay que importar redirect, esto te redirige a la función para hacerla de nuevo para limpiarla

    else:
        form = TaskForm()  # En el caso de que no se haya rellenado, lo inicializo vacío
    return render(
        request,
        "task/task_list.html",
        {"tasks": tasks, "form": form},
    )
