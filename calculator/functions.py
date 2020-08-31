"""
This document contains the functions used by the calculators
"""

#Función usada para calcular el precio final de un inmueble

def calcular_precio_final(precio_cliente, porcentaje_comision, includes_vat):
    precio_cliente = int(precio_cliente)
    porcentaje_comision = int(porcentaje_comision)

    if includes_vat == 'vat_included':
        print(includes_vat)
        precio_final = precio_cliente
        comision_agencia_iva = precio_final * porcentaje_comision / 100

        while (precio_final <= (precio_cliente + comision_agencia_iva)):
            precio_final += 1
            comision_agencia_iva = precio_final * porcentaje_comision / 100

        comision_neta_agencia = comision_agencia_iva / 1.21
        iva_operacion = comision_agencia_iva - comision_neta_agencia

    else: 
        precio_final = precio_cliente
        comision_neta_agencia = precio_final * porcentaje_comision / 100
        iva_operacion = comision_neta_agencia * 0.21

        while (precio_final <= (precio_cliente + comision_neta_agencia + iva_operacion)):
            precio_final += 1
            comision_neta_agencia = precio_final * porcentaje_comision / 100
            iva_operacion = comision_neta_agencia * 0.21
        
        comision_agencia_iva = comision_neta_agencia + iva_operacion

    return precio_final, comision_neta_agencia, iva_operacion, comision_agencia_iva

def calcular_neto_cliente(precio_final, porcentaje_comision, includes_vat):
    precio_final = int(precio_final)
    porcentaje_comision = int(porcentaje_comision)

    if includes_vat == 'vat_included':
        comision_agencia_iva = precio_final * porcentaje_comision/100
        iva_operacion = comision_agencia_iva * 0.21
        comision_neta_agencia = comision_agencia_iva - iva_operacion
        neto_cliente = precio_final - comision_agencia_iva

    else:
        comision_neta_agencia = precio_final * porcentaje_comision/100
        iva_operacion = comision_neta_agencia * 0.21
        comision_agencia_iva = comision_neta_agencia + iva_operacion
        neto_cliente = precio_final - comision_agencia_iva

    return neto_cliente, comision_neta_agencia, iva_operacion, comision_agencia_iva

def calcular_capital_inicial(tipo_de_inmueble, comprador_bonificado, nivel_ingresos_bonificado, valor_inmueble):
    aportacion_20_porciento = valor_inmueble * 0.2
    impuesto_ajd = valor_inmueble * 0.01
    gastos_notaria = valor_inmueble * 0.005
    registro = 180
    gestoria = 250
    tasacion = 300
    comision_de_apertura = valor_inmueble * 0.0075
    seguro_hogar = 150
    pretotal = aportacion_20_porciento + impuesto_ajd + gastos_notaria + registro + gestoria + tasacion + comision_de_apertura + seguro_hogar
    
    if tipo_de_inmueble == 'vivienda_nueva':
        iva_compra = valor_inmueble * 0.1
        total = pretotal + iva_compra
        return aportacion_20_porciento, iva_compra, impuesto_ajd, gastos_notaria, gestoria, tasacion, comision_de_apertura, seguro_hogar, total
    
    else: 
        if (comprador_bonificado == 'si' and nivel_ingresos_bonificado == 'si'):
            impuesto_transmisiones = valor_inmueble *0.05        
        else:
            impuesto_transmisiones = valor_inmueble * 0.1
        total = pretotal + impuesto_transmisiones
        return aportacion_20_porciento, impuesto_transmisiones, impuesto_ajd, gastos_notaria, gestoria, tasacion, comision_de_apertura, seguro_hogar, total


    
        
