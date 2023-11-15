from django.urls import path
from .views import Task_formulario, Task_todas, Task_descripcion

urlpatterns = [
    path("formulario/", Task_formulario.as_view(), name="task_formulario"),
    path("", Task_todas.as_view(), name="task_todas"),
    path("detalles/<int:pk>", Task_descripcion.as_view(), name="Task_descripcion"),
]
