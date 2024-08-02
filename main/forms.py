from django import forms


class FormularioLogin(forms.Form):
    email = forms.EmailField(label='Correo Electronico', required=True)  
    user_name = forms.CharField(label='Nombre de usuario', required=True)
    
    password = forms.CharField(
        label='Contraseña',
        required=True
    )
    confirm_password = forms.CharField(
        label='Confirmar contraseña',
        required=True
    )
    
class FormularioAprobando(forms.Form):
    user_name = forms.CharField(label='Nombre de usuario', required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)