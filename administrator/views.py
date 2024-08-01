from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import FormularioAdmin
from .models import Libros, Categorias, Categorias_Libros
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

def enviar(request):
    if request.method == 'POST':
        form = FormularioAdmin(request.POST, request.FILES)
        if form.is_valid():
            # Procesar datos del formulario
            imagen = form.cleaned_data['imagen']
            autor = form.cleaned_data['autor']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            titulo = form.cleaned_data['titulo']
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            categorias = form.cleaned_data['categorias']

            # Guarda el libro
            libro = Libros(
                Titulo=titulo,
                Autor=autor,
                Precio=precio,
                Descripcion=descripcion,
                Fecha_Publicacion=fecha_publicacion,
                Img_Portada=imagen,
            )
            libro.save()

            # Guarda las categorías
            for categoria in categorias:
                categoria_obj, created = Categorias.objects.get_or_create(Categorias=categoria)
                Categorias_Libros.objects.create(Id_Libros=libro, Id_Categorias=categoria_obj)

            return JsonResponse({'success': True, 'message': 'Libro guardado con éxito'})

        return JsonResponse({'success': False, 'message': 'Error al guardar el libro'})

    elif request.method == 'GET':
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            libros = Libros.objects.filter(Q(Titulo__icontains=busqueda))
            resultados = []
            for libro in libros:
                resultados.append({
                    'id': libro.Id_Libros,
                    'titulo': libro.Titulo,
                    'imagen': libro.Img_Portada.url if libro.Img_Portada else None,
                })
            return JsonResponse({'resultados': resultados})

    form = FormularioAdmin()
    return render(request, 'index.html', {'form': form})


def obtener_libro(request, libro_id):
    try:
        libro = get_object_or_404(Libros, Id_Libros=libro_id)
        categorias = Categorias_Libros.objects.filter(Id_Libros=libro).values_list('Id_Categorias__Id_Categorias', flat=True)
        
        data = {
            'success': True,
            'libro': {
                'id': libro.Id_Libros,
                'titulo': libro.Titulo,
                'autor': libro.Autor,
                'precio': libro.Precio,
                'descripcion': libro.Descripcion,
                'fecha_publicacion': libro.Fecha_Publicacion.strftime('%Y-%m-%d'),
                'imagen': libro.Img_Portada.url if libro.Img_Portada else None,
                'categorias': list(categorias)
            }
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

def eliminar_libro(request, libro_id):
    if request.method == 'POST':
        libro = get_object_or_404(Libros, Id_Libros=libro_id)
        libro.delete()
        return JsonResponse({'success': True, 'message': 'Libro eliminado con éxito'})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})