from django.urls import path
from .views import home
from .views import participantes, participante, winners

urlpatterns = [
    path('', home), 
    path('sorteo/<int:sorteo_id>/', participantes, name='participantes'),
    path('sorteo/participantes/<int:participante_id>/', participante, name='participante'),
    path('winners-for-peru/', winners, name='winners')
]

# agregar campo de nacionalidad, esto debe ser un fk a otro modelo a nacionalidad
# llenar modelo de nacionalidad con datos
# actualizar modelos de participantes con la nacionalidad
# mostrar solo los winners de peru
