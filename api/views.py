from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import RegistroHora
from django.db.models import F, DurationField, ExpressionWrapper
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def sumar_hora(request):
    hora1 = request.data.get('hora1')
    hora2 = request.data.get('hora2')

    try:
        resultado = RegistroHora.objects.create(
            hora=F('hora') + hora1,
            minutos=F('minutos') + hora2,
        )
        return Response(f"La hora y minutos sumados son: {resultado.hora}:{resultado.minutos}")
    except Exception as e:
        logger.exception(e)
        return Response(status=400)


@api_view(['DELETE'])
def borrar_registro(request, registro_id):
    try:
        RegistroHora.objects.filter(id=registro_id).delete()
        return Response("Registro borrado exitosamente")
    except Exception as e:
        logger.exception(e)
        return Response(status=400)


@api_view(['GET'])
def obtener_hora(request, registro_id):
    try:
        registro = RegistroHora.objects.get(id=registro_id)
        return Response(f"La hora es: {registro.hora}")
    except RegistroHora.DoesNotExist:
        return Response("Registro no encontrado", status=404)
    except Exception as e:
        logger.exception(e)
        return Response(status=400)


@api_view(['GET'])
def obtener_minutos(request, registro_id):
    try:
        registro = RegistroHora.objects.get(id=registro_id)
        minutos = registro.hora.hour * 60 + registro.hora.minute
        return Response(f"Los minutos son: {minutos}")
    except RegistroHora.DoesNotExist:
        return Response("Registro no encontrado", status=404)
    except Exception as e:
        logger.exception(e)
        return Response(status=400)


@api_view(['POST'])
def agregar_registro(request, registro_id_origen, registro_id_destino):
    try:
        registro_origen = RegistroHora.objects.get(id=registro_id_origen)
        registro_destino = RegistroHora.objects.get(id=registro_id_destino)

        resultado = RegistroHora.objects.create(
            hora=ExpressionWrapper(
                registro_destino.hora +
                (registro_origen.hora.hour * 3600 +
                 registro_origen.hora.minute * 60),
                output_field=DurationField()
            ),
            minutos=registro_destino.minutos + registro_origen.minutos
        )
        return Response(f"Registro agregado exitosamente. Hora y minutos: {resultado.hora}:{resultado.minutos}")
    except RegistroHora.DoesNotExist:
        return Response("Registro no encontrado", status=404)
    except Exception as e:
        logger.exception(e)
        return Response(status=400)
