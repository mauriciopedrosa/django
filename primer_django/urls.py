from django.contrib import admin
from django.urls import path
from .views import saludo, segunda_vista, dia_de_hoy, mi_nombre_es, probar_template


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('url_inesperada/', segunda_vista),
    path('fecha/', dia_de_hoy),
    path('nombre/<nombre>', mi_nombre_es),
    path('template-1', probar_template),
]
