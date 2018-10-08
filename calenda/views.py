from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Entrada
from .forms import FormularioEntrada


# Create your views here.
# El render recibe el request, el template y el contexto
def index(request):
    # Al agregar el redirect para el login se comenta esto y solamente se redirecciona el index.html
    # entradas = Entrada.objects.all()
    # return render(request,'calenda/index.html',{'entradas':entradas})
    return render(request, 'calenda/index.html')

@login_required
def calendar(request):
    # entradas = Entrada.objects.all()
    entradas = Entrada.objects.filter(autor=request.user)

    return render(request, 'calenda/calendar.html', {'entradas': entradas})

@login_required
def detalles(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'calenda/detalles.html', {'entrada': entrada})

@login_required
def agregar(request):
    if request.method == 'POST':
        form = FormularioEntrada(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            descripcion = form.cleaned_data['descripcion']

            Entrada.objects.create(
                nombre=nombre,
                autor = request.user,
                fecha=fecha,
                descripcion=descripcion,
            ).save()

            return HttpResponseRedirect('/calendar')

    else:
        form = FormularioEntrada()

    return render(request, 'calenda/agregar.html', {'form': form})

@login_required
def eliminar(request, pk):
    if request.method == 'DELETE':
        entrada = get_object_or_404(Entrada, pk=pk)
        entrada.delete()
    return HttpResponseRedirect('/')

def registrate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/calendar')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registrate.html', {'form': form})

def tarea(request):
    return render(request,'prebes/tarea.html')