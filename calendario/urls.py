from django.contrib import admin
from django.urls import path
from calenda import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entrada/<int:pk>',views.detalles,name='detalles'),
    path('entrada/agregar',views.agregar,name='agregar'),
    path('admin/', admin.site.urls),
]
