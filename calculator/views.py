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
        return render(request, 'calculator/precio_final_result.html', {'context': context})

def neto_cliente(request):
    if request.method == "GET":
        return render(request, 'calculator/neto_cliente.html')
    else:
        context = functions.calcular_neto_cliente(request.POST['precio_final'], 
        request.POST['porcentaje_comision'], request.POST['includes_vat'])
        return render(request, 'calculator/neto_cliente_result.html', {'context': context})
    

def capital_inicial(request):
    if request.method == "GET":
        return render(request, 'calculator/capital_inicial.html')
    else:
        valores = functions.calcular_capital_inicial(request.POST['tipo_de_inmueble'], request.POST['comprador_bonificado'], request.POST['nivel_ingresos'], int(request.POST['valor_inmueble']))
        gastos = ['aportación del 20%', 'IVA (vivienda nueva) o ITP (vivienda usada)', 'Impuesto AJD-hipotecas', 'Gastos de notaría', 'Gestoría', 'Tasación', 'Comisión de apertura *', 'Seguro hogar*', 'Total']
        context = zip(valores, gastos)
        return render(request, 'calculator/capital_inicial_result.html', {'context': context})

def comision_agencia(request):
    if request.method == "GET":
        return render(request, 'calculator/comision_agencia.html')
    else:
        context = functions.calcular_comision_agencia(int(request.POST['precio_inmueble']), int(request.POST['porcentaje_comision']), request.POST['includes_vat'])
        return render(request, 'calculator/comision_agencia_result.html', {'context': context})

def comision_agente(request):
    if request.method == "GET":
        return render(request, 'calculator/comision_agente.html')
    else:
        comision_agente_neta = functions.calcular_comision_agente(int(request.POST['precio_inmueble']), int(request.POST['porcentaje_comision']), 
        request.POST['includes_vat'], int(request.POST['porcentaje_agente']))
        comision_agente_iva = comision_agente_neta * 0.21
        comision_agente_mas_iva = comision_agente_neta + comision_agente_iva
        context = [comision_agente_neta, comision_agente_iva, comision_agente_mas_iva]
        return render(request, 'calculator/comision_agente_result.html', {'context': context})

def gastos_vendedor(request):
    if request.method == "GET":
        return render(request, 'calculator/gastos_vendedor.html')
    else:
        plusvalua_municipal = functions.calcular_plusvalua_municipal(request.POST['municipio'], int(request.POST['año_de_adquisicion']), int(request.POST['valor_de_adquisicion']), int(request.POST['año_de_venta']), int(request.POST['valor_de_venta']), int(request.POST['valor_catastral']))
        plusvalua_IRPF = functions.calcular_plusvalua_estatal(int(request.POST['valor_de_adquisicion']), int(request.POST['valor_de_venta']), int(request.POST['inversiones']), int(request.POST['rendimiento']), request.POST['edad_vendedor'], request.POST['vender_2_años'])
        total_gastos = plusvalua_municipal + plusvalua_IRPF
        context = [plusvalua_municipal, plusvalua_IRPF, total_gastos]
        return render(request, 'calculator/gastos_vendedor_result.html', {'context' : context})

