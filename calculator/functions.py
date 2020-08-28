"""
This document contains the functions used by the calculators
"""

#Función usada para calcular el precio final de un inmueble

def calcular_precio_final(precio_cliente, porcentaje_comision, includes_vat):
    precio_cliente = int(precio_cliente)
    porcentaje_comision = int(porcentaje_comision)

    if includes_vat == 'includes_vat':
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