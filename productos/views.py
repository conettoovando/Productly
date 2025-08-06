from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.

# With api rest
# # /productos
# def index(request):
#     # Este metodo sirve para retornar una respuesta JSON como una api, lo mejor es utilizar una dependencia como Django Rest Framework
#     productos = Producto.objects.all().values()
#     # productos = Producto.objects.filter(puntaje__gte=3)
#     # productos = Producto.objects.get(pk=1) # Obtiene solo 1 producto
#     # print(productos)
#     return JsonResponse(list(productos), safe=False)

# /productos
def index(request):
    productos = Producto.objects.all()

    return render(
        request,
        'index.html',
        context={
            'productos': productos,
        }
    )

def detalle(request, producto_id):
    # try:
    #     producto = Producto.objects.get(id=producto_id)

    #     return render(
    #         request,
    #         'detalle.html',
    #         context={
    #             'producto': producto
    #         }
    #     )
    # except Producto.DoesNotExist:
    #     raise Http404()
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={
            'producto': producto
        }
    )

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')

    else: form = ProductoForm() # Si no es una petición POST, crea un formulario vacío

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )