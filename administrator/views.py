from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormularioAdmin
from .models import Libros, Categorias, Categorias_Libros

def admin(request):
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

    else:
        form = FormularioAdmin()

    return render(request, 'index.html', {'form': form})
