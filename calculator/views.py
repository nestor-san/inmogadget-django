from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from calculator import functions

def index(request):
    return render(request, 'calculator/index.html')

def precio_final(request):
    if request.method == "GET":
        return render(request, 'calculator/precio_final.html')
    else:
        context = functions.calcular_precio_final(request.POST['precio_cliente'], 
        request.POST['porcentaje_comision'], request.POST['includes_vat'])
        return render(request, 'calculator/precio_final_result.html', {'context': context, 'testvat':request.POST['includes_vat']})

def neto_cliente(request):
    return render(request, 'calculator/neto_cliente.html')

def capital_inicial(request):
    return render(request, 'calculator/capital_inicial.html')

def comision_agencia(request):
    return render(request, 'calculator/comision_agencia.html')

def comision_agente(request):
    return render(request, 'calculator/comision_agente.html')

