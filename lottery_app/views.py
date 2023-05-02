from django.shortcuts import render
from .models import Sorteo, Participante
import os

# Por este endPoint podemos ver los registros de sorteos
def home(request):
    sorteos = Sorteo.objects.all()
    hostname = os.environ.get('HOSTNAME')
    return render(request, 'lottery_app/home.html', {'sorteos': sorteos, 'hostname': hostname})


def participantes(request, sorteo_id):
    participantes = Participante.objects.filter(sorteo_id=sorteo_id)
    return render(request, 'lottery_app/participantes.html', {'participantes': participantes})


def participante(request, participante_id):
    participante = Participante.objects.filter(id=participante_id).first()
    return render(request, 'lottery_app/participante.html', {'participante': participante})


def winners(request):
    #contains: contiene parte o todo del query
    #icontains: contiene parte o todo del query sin importar upperCase or lower
    #exac: contiene todo del query
    #iexac: contiene todo del query sin importar upperCase or lower
    winners = Participante.objects.filter(ganador=True, nacionalidad__pais__exact='Peru')
    return render(request, 'lottery_app/winner.html', {'winners': winners})
