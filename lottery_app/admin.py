from django.contrib import admin
from .models import Sorteo


@admin.register(Sorteo)
class SorteoAdmin(admin.ModelAdmin):
    pass
