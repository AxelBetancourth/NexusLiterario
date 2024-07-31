from django import forms

class FormularioAdmin(forms.Form):
    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={'id': 'img_input'}))
    autor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'autor_input', 'placeholder': 'Autor...'}))
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'fecha_publicacion'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'titulo_input', 'placeholder': 'Título...'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'precio_input'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'id': 'descripcion_input', 'placeholder': 'Descripción...'}))

    # Agrega un campo para manejar las categorías
    categorias = forms.MultipleChoiceField(
        choices=[
            ('miedo', 'Miedo'),
            ('romance', 'Romance'),
            ('accion', 'Acción'),
            ('misterio', 'Misterio'),
            ('historia', 'Historia'),
            ('aventura', 'Aventura'),
            ('economia', 'Economía'),
            ('biografias', 'Biografías'),
            ('ciencia', 'Ciencia'),
            ('literatura', 'Literatura'),
            ('fantasia', 'Fantasía'),
            ('medicina', 'Medicina'),
            ('programacion', 'Programación'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
