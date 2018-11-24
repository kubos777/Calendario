from django import forms

class FormularioEntrada(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha = forms.DateTimeField()
    descripcion = forms.CharField(widget=forms.Textarea)
    