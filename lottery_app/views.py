from django.shortcuts import render
from .models import Sorteo


def home(request):
    sorteos = Sorteo.objects.all()
    return render(request, 'lottery_app/home.html', {'sorteos': sorteos})