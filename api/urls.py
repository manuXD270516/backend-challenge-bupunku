from django.contrib import admin
from django.urls import path
from api.views import sumar_hora, borrar_registro, obtener_hora, obtener_minutos, agregar_registro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sumar_hora/', sumar_hora, name='sumar_hora'),
    path('borrar_registro/<int:registro_id>/',
         borrar_registro, name='borrar_registro'),
    path('obtener_hora/<int:registro_id>/', obtener_hora, name='obtener_hora'),
    path('obtener_minutos/<int:registro_id>/',
         obtener_minutos, name='obtener_minutos'),
    path('agregar_registro/int:registro_id_origen/int:registro_id_destino/',
         agregar_registro, name='agregar_registro'),
]
