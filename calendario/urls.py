from django.contrib import admin
from django.urls import path
from django.contrib.auth import  views as auth_views
from calenda import views

urlpatterns = [
    path('',views.index,name='index'),
    path('calendar',views.calendar,name='calendar'),
    path('login',auth_views.login,name='login'),
    path('registrate',views.registrate,name='registrate'),
    path('logout',auth_views.logout,{'next_page':'/'},name='logout'),
    path('entrada/<int:pk>',views.detalles,name='detalles'),
    path('entrada/agregar',views.agregar,name='agregar'),
    path('entrada/eliminar/<int:pk>',views.eliminar,name='eliminar'),
    path('prebes/37/tarea',views.tarea,name="tarea"),
    path('admin/', admin.site.urls),
]

