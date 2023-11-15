from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from django.views import View
from .forms import (
    TaskForm,
)  # Hay que importar el formulario que he generado en el archivo forms, TaskForm es la clase


# Create your views here.

"""
#De esta forma guardamos en la base de datos sin form.save
class Task_list(View):
    template_name = "task/task_list.html"
    form = TaskForm()

    def actualizaTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        tasks = Task.objects.all()
        form = self.form
        return render(
            request, self.template_name, {"form": form, "tasks": self.actualizaTask()}
        )

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():#Si es válido, limpiamos los campos ya que 
            nombre = form.cleaned_data["nombre"]
            descripcion = form.cleaned_data["descripcion"]
            realizada = form.cleaned_data["realizada"]

            task_nuevo = Task(
                nombre=nombre, descripcion=descripcion, realizada=realizada
            )
            task_nuevo.save()

            # form.save() Hay que buscar cómo guardarlo en la base de datos
            return redirect("task_list")
        return render(
            request, self.template_name, {"form": form, "tasks": self.actualizaTask()}
        )
"""


class Task_formulario(View):
    template_name = "task/task_list_con_formulario.html"
    form = TaskForm()

    def actualizaTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        form = self.form
        return render(
            request, self.template_name, {"form": form, "tasks": self.actualizaTask()}
        )

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_formulario")
        return render(
            request, self.template_name, {"form": form, "tasks": self.actualizaTask()}
        )


class Task_todas(View):
    template_name = "task/task_list.html"

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {"tasks": tasks})


class Task_descripcion(View):
    template_name = "task/task_descripcion.html"

    def get(self, request, pk):
        task_descripcion = get_object_or_404(Task, pk=pk)
        return render(
            request, self.template_name, {"task_descripcion": task_descripcion}
        )


# Clases

"""

Métodos
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
"""
