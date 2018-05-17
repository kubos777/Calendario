from django.contrib import admin
from django.urls import path
from calenda import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entrada/<int:pk>',views.detalles,name='detalles'),
    path('admin/', admin.site.urls),
]
