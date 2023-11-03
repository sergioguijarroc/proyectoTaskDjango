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
Añadimos la siguiente línea al final del archivo:

```
STATIC_ROOT = BASE_DIR / 'static'
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