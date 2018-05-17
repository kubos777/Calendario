from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#El render recibe el request, el template y el contexto
def index(request):
    return render(request,'calenda/index.html')
