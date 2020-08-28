from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='index'),
    path('precio_final/', views.precio_final, name='precio_final'),
    path('neto_cliente/', views.neto_cliente, name='neto_cliente'),
    path('capital_inicial/', views.capital_inicial, name='capital_inicial'),
    path('comision_agencia/', views.comision_agencia, name='comision_agencia'),
    path('comision_agente/', views.comision_agente, name='comision_agente'),
]