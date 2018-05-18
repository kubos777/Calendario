from django.contrib import admin
from django.urls import path
from calenda import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entrada/<int:pk>',views.detalles,name='detalles'),
    path('entrada/agregar',views.agregar,name='agregar'),
    path('entrada/eliminar/<int:pk>',views.eliminar,name='eliminar'),
    path('admin/', admin.site.urls),
]

