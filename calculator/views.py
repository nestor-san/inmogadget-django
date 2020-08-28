from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'calculator/index.html')

def precio_final(request):
    return render(request, 'calculator/precio_final.html')

def neto_cliente(request):
    return render(request, 'calculator/neto_cliente.html')

def capital_inicial(request):
    return render(request, 'calculator/capital_inicial.html')

def comision_agencia(request):
    return render(request, 'calculator/comision_agencia.html')

def comision_agente(request):
    return render(request, 'calculator/comision_agente.html')

