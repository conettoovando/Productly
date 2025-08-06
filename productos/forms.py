from . import models
from django.forms import ModelForm # Se instala aparte el paquete django.forms para crear formularios basados en modelos en settings.py

class ProductoForm(ModelForm):
    class Meta: # Meta class to define form properties
        model = models.Producto # Especifica el modelo asociado al formulario
        fields = ['nombre', 'stock', 'puntaje', 'categoria'] # Especifica los campos que se incluirán en el formulario

