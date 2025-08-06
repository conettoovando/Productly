Iniciar proyecto con django

Primero se debe instalar django ya sea en un entorno virtual el cual es altamente recomendable

pipenv install django

Luego de haberlo instalado crear el proyecto en la carpeta que se desee, se utiliza un . al final para crearlo dentro de la carpeta donde se ejecute el comando

django-admin startproject [Nombre del proyecto] [.]

Esto deplegara una carpeta con el nombre del proyecto que contiene distintos archivos

- \_\_init\_\_
- asgi
- settings
- urls
- wsgi

1. init es para poder transformar la carpeta con el nombre del proyecto en un paquete
2. settings es un archivo donde se colocan diferentes configuraciones del proyecto
3. urls donde se configuran las rutas de la aplicacion

Para ejecutar el servidor se hace con el comando: **python .\manage.py runserver** Usando el archivo manage.py creado al iniciar el proyecto con django

Para crear una aplicacion dentro del proyecto con el servidor apagado se debe ejecutar el comando:

python manage.py startapp ["Nombre de la aplicacion"]

Esto creara una carpeta con el nombre de la aplicacion que incluye

- Carpeta migrations
- \_\_init\_\_
- admin.py
- apps.py
- models.py
- tests.py
- views.py

1. migrations se encarga de mantener los cambios que se realizan a una base de datos
2. \_\_init\_\_ indica que es un paquete
3. admin registra los modelos en el administrador de django
4. apps Se registra la aplicacion
5. models permite definir clases las cuales harán referencia a tablas en la base de datos
6. tests podemos escribir test automatizados

para seguir con la aplicacion se debe

- instalar la aplicacion
- instancias las urls
- indicar en views lo que debe ejecutar la ruta

Para instalar el la aplicacion se debe ir a la ruta de la aplicacion y dentro del archivo apps.py copiar el nombre de la clase que ha sido creado y pegarlo entre ""
en un listado dentro de settings de la configuracion del proyecto en "INSTALED_APPS"
Ejemplo: "productos.apps.ProductosConfig"

Luego se define la ruta en la carpeta del proyecto, en este caso productly y en el archivo urls.py se debe definir la ruta con la convension similar a la que se utiliza
Para incluir la aplicacion se debe importar include dentro de settings y llamar al paquete mediante esa funcion
Dentro de la aplicacion en este caso "productos" se debe crear un archivo urls.py

Luego se debe definir una vista en views.py dentro de la aplicacion y asi al ejecutar el servidor ya queda definida una ruta y una vista para esa aplicacion en este caso localhost:[port]/productos

# Migraciones:

Las migraciones es para vincular los modelos creados con la base de datos insertandolos dentro.

Para realizar las migraciones se realiza con el codigo en consolda de:

1. Crear migraciones: _python .\manage.py makemigrations_
2. Migrar: _python .\manage.py migrate_

PANEL DE ADMINISTRACION:
Para crear un administrador y poder acceder a la ruta http://127.0.0.1:8000/admin Se debe crear un usuario mediante un comando:
python manage.py createsuperuser Y completar el registro del usuario

Una vez dentro se vera el panel de administracion el cual puede no visualizar todos los modelos que se encuentren para eso hay que configurarlo
dentro del archivo admin.py dentro de la aplicacion.

con la funciones: admin.site.register()

PARA EVITAR ERRORES CON VS CODE:
instalar pylintrc para django con:
pipenv install pylint-django

luego en la ruta del proyecto completo, es decir donde se encuentras los pipfile y el manage.py crear un archivo llamado .pylintrc donde cargar los plugins con:
load-plugins=pylint-django

PERSONALIZAR FOMULARIOS
Para personalizar los estilos de formularios seguir los pasos de forms.py dentro de producto y además estructurar la carpeta templates con la ruta de github de django

https://github.com/django/django/tree/main/django/forms/templates/django/forms/widgets
django/django/forms/templates/django/forms/widgets/input.html
