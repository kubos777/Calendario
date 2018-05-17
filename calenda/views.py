from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Entrada
# Create your views here.
#El render recibe el request, el template y el contexto
def index(request):
    entradas = Entrada.objects.all()
    return render(request,'calenda/index.html',{'entradas':entradas})

def detalles(request,pk):
    entrada = get_object_or_404(Entrada,pk = pk)
    return render(request,'calenda/detalles.html',{'entrada':entrada})
