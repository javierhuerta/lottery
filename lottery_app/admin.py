from django.contrib import admin
from .models import Sorteo
from .models import Participante, Nacionalidad


@admin.register(Sorteo)
class SorteoAdmin(admin.ModelAdmin):
    pass

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    pass

@admin.register(Nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    pass