# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# segundo taller del segundo corte...........!!!!
# =============================================================================
# =============================================================================
# 1. El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:
# DIGITO COLOR
# 1 o 2 Amarilla
# 3 o 4 Rosa
# 5 o 6 Roja
# 7 u 8 Verde
# 9 o 0 Azul
# =============================================================================
placas = []
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
cantidad = int(input('Ingresa la cantidad de autos: '))
for x in range(cantidad):
    placa = input(f'Ingrese la placa N°{x + 1}: ')
    placa = int(placa)
    placas.append(placa)
    if 1 in placas or 2 in placas:
        amarillo = amarillo + 1
    if 3 in placas or 4 in placas:
        rosa = rosa + 1
    if 5 in placas or 6 in placas:
        roja = roja + 1
    if 7 in placas or 8 in placas:
        verde = verde + 1
    if 9 in placas or 0 in placas:
        azul = azul + 1
        
        
print('cantidad de sticker amarillo es: ',amarillo)
print('cantidad de sticker rosa es: ',rosa)
print('cantidad de sticker roja es: ',roja)
print('cantidad de sticker verde es: ',verde)
print('cantidad de sticker azul es: ',azul)