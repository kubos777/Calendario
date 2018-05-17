from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entrada
from .forms import FormularioEntrada
# Create your views here.
#El render recibe el request, el template y el contexto
def index(request):
    entradas = Entrada.objects.all()
    return render(request,'calenda/index.html',{'entradas':entradas})

def detalles(request,pk):
    entrada = get_object_or_404(Entrada,pk = pk)
    return render(request,'calenda/detalles.html',{'entrada':entrada})

def agregar(request):
    if request.method == 'POST':
        form = FormularioEntrada(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            descripcion = form.cleaned_data['descripcion']

            Entrada.objects.create(
                nombre = nombre,
                fecha = fecha,
                descripcion = descripcion,
            ).save()

            return HttpResponseRedirect('/')

    else:
        form = FormularioEntrada()

    return render(request,'calenda/agregar.html',{'form':form})
