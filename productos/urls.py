from django.urls import path
from . import views

app_name = 'productos' # Espacio de nombres para las URLs de la aplicación productos
urlpatterns = [
    path('', views.index, name='index'), # Ruta para la vista principal de productos
    path('formulario', views.formulario, name='formulario'),
    path('<int:producto_id>', views.detalle, name='detalle') # name es indispensable para referenciar la vista en templates o redirecciones
]