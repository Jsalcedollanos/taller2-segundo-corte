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

# =============================================================================
# 2. Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
# 40.
# =============================================================================
animales = []
cantidad = int(input('Ingrese la cantidad de animales: '))
elefantes = 0
jirafa = 0
chimpances = 0
categoria1 = 0
categoria2 = 0
categoria3 = 0
porcentaje1 = 0
porcentaje2 = 0
porcentaje3 = 0
for x in range(cantidad):
    edad = int(input('Ingrese la edad del animal: '))
    animales.append(edad)
    
    
for x in range(cantidad):
    if animales[x] >= 0 and animales[x] <= 1:
        categoria1 = categoria1 + 1
        porcentaje1 = int(categoria1 * cantidad) 
        
    if animales[x] > 1 and animales[x] < 3:
        categoria2 = categoria2 + 1
        porcentaje2 = int(categoria2 * cantidad)
        
    if animales[x] >= 3:
        categoria3 = categoria3 + 1
        porcentaje3 = int(categoria3 * cantidad)
        
p = int(input('Que animal desea seleccionar? (1)Elefante (2)Jirafa (3)Chimpanses : '))

if (p > 3):
    print('Oohh espera... la especimen que intentas escoger no se encuentra registrada! Atento a tu seleccion...')
        
if p == 1:
    print(f'Se escogera {cantidad} Elefantes aleatoriamente')
if p == 2:
    print(f'Se escogera {cantidad} Jirafas aleatoriamente')
if p == 3:
    print(f'Se escogera {cantidad} Chimpanses aleatoriamente')
    

        
print(f'Cantidad de animales en la categoria 1 de (0 a 1 años es): {porcentaje1}%')
print(f'Cantidad de animales en la categoria 2 de (Mas de 1 años y menor de 3 años): {porcentaje2}%')
print(f'Cantidad de animales en la categoria 3 de (Mas de 3 años es): {porcentaje3}%')

# =============================================================================
# 3. Una empresa se requiere calcular el salario semanal de cada uno de los n
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de
# lasprimeras 40 horas y $25 por cada hora extra.
# =============================================================================
obreros = []
cantidad = int(input('Ingrese cantidad de trabajadores de su compañia: '))
for x in range(cantidad):
        horas = int(input('Ingrese cantidad de horas: '))
        obreros.append(horas)
        
for x in range(cantidad):
    if obreros[x] <= 40:
        salario = int(obreros[x] * 20)
        print(f'El salario del obrero {x + 1} es: ',salario)
    if obreros[x] > 40:
        he = obreros[x] - 40
        salario1 = (obreros[x] - he) * 40
        salario2 = he * 25
        salarioTotal = int(salario1 + salario2)
        print(f'El salario del obrero {x + 1} es: ',salarioTotal)
        
# =============================================================================
# 4. Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.
# =============================================================================

acuHombre = 0
acuMujer = 0
acuAlumno = 0

cantHombres = int(input('Cantidad de hombres: '))      
cantMujeres = int(input('Cantidad de mujeres: '))
cantAlumnos = int(input('Cantidad de alumnos: '))

contHombres = 0
contMujeres = 0
contAlumnos = 0

for i in range(cantHombres):
    edad =   int(input(f'Genero(Hombre){i + 1} Ingrese edad: '))
    acuHombre = acuHombre + edad
    promeHombres = acuHombre / cantHombres
    
for i in range(cantMujeres):
    edad =   int(input(f'Genero(Mujer){i + 1} Ingrese edad: '))
    acuMujer = acuMujer + edad
    promeMujeres = acuMujer / cantMujeres
    
for i in range(cantAlumnos):
    edad =   int(input(f'Alumno {i + 1} Ingrese edad: '))
    acuAlumno = acuAlumno + edad
    promeAlumnos = acuAlumno / cantAlumnos
    
print('Promedio de edades de hombres es: ',promeHombres)
print('Promedio de edades de Mujeres es: ',promeMujeres)
print('Promedio de edades de alumnos es: ',promeAlumnos)
    
    


        
        