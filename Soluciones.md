Primero, abrimos una terminal en visual studio Code y creamos un entorno virtual con el comando:

```
python3 -m venv virtualTask
```

Luego, lo activamos con el comando:

```
source virtualTask/bin/activate
```

Previamente, tenemos que tener python instalado, importante estar dentro de un entorno virtual.

Para instalar Django, crearemos un archivo llamado requirements.txt que conendrá lo siguiente:
Django~=4.2.7 (o la versión que sea)

Después haremos:

```
pip install -r requirements.txt
```

Antes de continuar, crearemos un archivo .gitignore en la raíz del proyecto para subir a Github solo lo que nos interesa.

Ese archivo contendrá lo siguiente:

_.pyc
_~
**pycache**
myvenv
db.sqlite3
/static
.DS_Store

Una vez hecho, iniciaremos el proyecto de Django con el comando:

```
django-admin startproject mySite .
```

Ya tenemos creado el proyecto, ahora, vamos a modificar el archivo settings.py para que se pueda conectar a la base de datos.
En LANGUAGE_CODE ponemos ‘es-es’
En TIME_ZONE Deberíamos poner “Europe/Berlin”
Añadimos la siguiente línea al final del archivo para que se pueda conectar a la base de datos:

```
STATIC_ROOT = BASE_DIR / 'static'
```
```

Ahora, vamos a crear la base de datos:

```
python manage.py migrate
```

Ahora, vamos a compronbar que todo funciona correctamente:

```
python manage.py runserver
```

## Creación del modelo de nuestra app Task

Para mantener todo en orden, crearemos una aplicación separada dentro de nuestro proyecto.
Usaremos el siguiente comando:

    ```
    python manage.py startapp task
    ```

Después de crear la aplicación, vamos a añadirla a nuestro proyecto. Para ello, abrimos el archivo settings.py y añadimos la aplicación en la lista INSTALLED_APPS.
Añadiremos la siguiente línea:

    ```
    'task.apps.TaskConfig', #Ponemos el nombre de la aplicación y el nombre de la clase
    ```

Vamos a crear el modelo de nuestra aplicación. Para ello, abrimos el archivo models.py y añadimos el siguiente código:

    ```
    from django.db import models
    from django.utils import timezone

    class Task(models.Model):
        Nombre = models.CharField(max_length=200)
        descripcion = models.TextField()
        realizada = models.BooleanField(default=False)

        def __str__(self):
            return self.Nombre
        ```

## Actualizar cambios en la base de datos

Ahora, vamos reflejar los cambios en nuestra base de datos, para ello, ejecutaremos el siguiente comando:

    ```
    python manage.py makemigrations task #Nombre de la aplicación que queremos migrar, si no ponemos nada, se migrarán todas las aplicaciones
    ```

Ahora, vamos a aplicar los cambios en la base de datos:

        ```
        python manage.py migrate
        ```

## Administrador de nuestro sitio

Tenemos que abrir el archivo admin.py y añadir el siguiente código:

        ```
        from django.contrib import admin
        from .models import Task

        admin.site.register(Task)
        ```

### Crear un superusuario

Para ello, ejecutamos el siguiente comando:

```
python manage.py createsuperuser
```

Ejecutamos el servidor para comprobar que se han realizado los cambios:

```
python manage.py runserver
```

Si nos vamos a la dirección http://127.0.0.1:8000/admin y nos logueamos con el usuario y contraseña que hemos creado, podremos ver que se ha creado la tabla Task.

Vamos a añadir algunos datos para comprobar que todo funciona correctamente.

## URLS

Vamos a gestionar las urls, para ello vamos a crear un archivo urls.py en la carpeta task y añadiremos el siguiente código:

        ```
        from django.urls import path, include #Importamos include

        urlpatterns = [
            path('', include('task.urls')), #Añadimos la url de nuestra aplicación
        ]
        ```

Ahora, vamos a crear un archivo urls.py en la carpeta task y añadiremos el siguiente código:

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
                path('', views.task_list, name='task_list'),
        ]
        ```

## Creamos la vista

Vamos a poner el siguiente método en el archivo views.py

```
from django.shortcuts import render
from .models import Task #Esto

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task/task_list.html", {})
```

## Plantillas

Vamos a crear un directorio en task llamado templates, y, dentro de él, otro llamado task
En él, vamos a crear el archivo task_list.html
Y ahí vamos a introducir el siguiente

<h1>Task</h1>
<div>
  <ul>
    {%for task in tasks%}
    <li>
      {{task.nombre}} - {{task.descripcion}}<br />
      ¿Está hecha?
      <br />
      ({{task.realizada|yesno:"Sí,No"}})
    </li>
    {%empty%}
    <li>No hay tareas por hacer</li>
    {%endfor%}
  </ul>
</div>

Iniciamos el servidor y ya debería funcionar.
