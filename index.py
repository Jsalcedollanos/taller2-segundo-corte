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
    
# =============================================================================
# 5. Encontrar el menor valor de un conjunto de n números dados   
# =============================================================================
numeros=[]
cant = int(input('Ingrese la cantidad de numeros que desea calcular: '))
for x in range(cant):
    valor=int(input("Ingrese el numero:"))
    numeros.append(valor)

menor=numeros[0]
for x in range(1,cant):
    if numeros[x]<menor:
        menor=numeros[x]

print("Serie de numeros: ")
print(numeros)
print("El numero menor de la serie de numeros es: ",menor)

# =============================================================================
# Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. 
# Si existe diferencia positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso    
# =============================================================================
pesos1 = []
pesos2 = []
pesos3 = []
pesos4 = []
pesos5 = []
acu1 = 0
acu2 = 0
acu3 = 0
acu4 = 0
acu5 = 0

persona1Nombre = input('Ingrese su Nombre: ')
promedioAnterior1 = float(input('Ingrese Promedio anterior: ')) 
for i in range(10):
    peso1 = float(input(f'{persona1Nombre} Ingrese su peso para la báscula N°{i + 1}: '))
    pesos1.append(peso1)
    
for i in range(10):
    acu1 = acu1 + pesos1[i]

promedio1 = acu1 / 10

# =============================================================================
# 
# =============================================================================

persona2Nombre = input('Ingrese su Nombre: ')
promedioAnterior2 = float(input('Ingrese Promedio anterior: ')) 
for i in range(10):
    peso2 = float(input(f'{persona2Nombre} Ingrese su peso para la báscula N°{i + 1}: '))
    pesos2.append(peso2)
    
for i in range(10):
    acu2 = acu2 + pesos2[i]

promedio2 = acu2 / 10

# =============================================================================
# 
# =============================================================================

persona3Nombre = input('Ingrese su Nombre: ')
promedioAnterior3 = float(input('Ingrese Promedio anterior: ')) 
for i in range(10):
    peso3 = float(input(f'{persona2Nombre} Ingrese su peso para la báscula N°{i + 1}: '))
    pesos3.append(peso3)
    
for i in range(10):
    acu3 = acu3 + pesos3[i]

promedio3 = acu3 / 10

# =============================================================================
# 
# =============================================================================

persona4Nombre = input('Ingrese su Nombre: ')
promedioAnterior4 = float(input('Ingrese Promedio anterior: ')) 
for i in range(10):
    peso4 = float(input(f'{persona4Nombre} Ingrese su peso para la báscula N°{i + 1}: '))
    pesos4.append(peso4)
    
for i in range(10):
    acu4 = acu4 + pesos4[i]

promedio4 = acu4 / 10

# =============================================================================
# 
# =============================================================================

persona5Nombre = input('Ingrese su Nombre: ')
promedioAnterior5 = float(input('Ingrese Promedio anterior: ')) 
for i in range(10):
    peso5 = float(input(f'{persona5Nombre} Ingrese su peso para la báscula N°{i + 1}: '))
    pesos5.append(peso5)
    
for i in range(10):
    acu5 = acu5 + pesos5[i]

promedio5 = acu5 / 10



     
print(f'Promedio de peso de {persona1Nombre} es: ',promedio1)
print(f'Promedio de peso de {persona2Nombre} es: ',promedio2)
print(f'Promedio de peso de {persona3Nombre} es: ',promedio3)
print(f'Promedio de peso de {persona4Nombre} es: ',promedio4)
print(f'Promedio de peso de {persona5Nombre} es: ',promedio5)
        
if promedio1 > promedioAnterior1:
    print(f'{persona1Nombre} SUBIO')
else:
     print(f'{persona1Nombre} SUBIO')
     
if promedio2 > promedioAnterior2:
    print(f'{persona2Nombre} SUBIO')
else:
     print(f'{persona2Nombre} SUBIO')
     
if promedio3 > promedioAnterior3:
    print(f'{persona3Nombre} SUBIO')
else:
     print(f'{persona3Nombre} SUBIO') 

if promedio4 > promedioAnterior4:
    print(f'{persona4Nombre} SUBIO')
else:
     print(f'{persona4Nombre} SUBIO')
     
if promedio5 > promedioAnterior5:
    print(f'{persona5Nombre} SUBIO')
else:
     print(f'{persona5Nombre} SUBIO')        
     
# =============================================================================
# 7. En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artóculo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.
# =============================================================================

acu = 0
i = 1
while i == 1:
    articulo = input('Ingrese nombre del articulo: ')
    valor = int(input('Ingrese el valor del producto: '))
    cantidad = int(input(f'Cantidad de {articulo}: '))
    valorT = valor * cantidad
    acu = acu + valorT
    i = int(input('¿Desea ingresar otro producto? 1.(si) 2.(no): '))
    

print('Valor total es: ',acu)

# =============================================================================
#8. Un teatro otorga descuentos según la edad del cliente, determinar la
# cantidad del dinero que el teatro deja de percibir por cada ua de las
# categorias. Tomar en cuenta que los niños menores de 5 años no pueden
# entrar al teatro y que existe un precio único en los asientos. Los descuentos
# se hacen tomando en cuenta el siguiente cuadro:
# Edad % Descuento
# 5 – 14 35%
# 15-19 25%
# 20 – 45 10%
# 46 – 65 25%
# 66 en Adelante 35%
# =============================================================================
acu1 = 0
acu2 = 0
acu3 = 0
acu4 = 0
acu5 = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
asiento = 0
i = 1
while i == 1:
    
    edad = int(input('Ingrese edad del usuario: '))
    if (edad > 5 or edad <= 14):
        asiento = 5000
        descuento1 = asiento * 0.35
        total1 = asiento - descuento1
        acu1 = acu1 + total1
        print('entro aqui')
    elif (edad >= 15 or edad <= 19):
        asiento = 5000
        descuento2 = asiento * 0.25
        total2 = asiento - descuento2
        acu2 = acu2 + total2
        print('entro aqui')
    elif (edad >= 20 or edad <= 45):
        asiento = 5000
        descuento3 = asiento * 0.10
        total3 = asiento - descuento3
        acu3 = acu3 + total3
        print('entro aqui')
    elif (edad >= 46 or edad <= 65):
        asiento = 5000
        descuento4 = asiento * 0.25
        total4 = asiento - descuento4
        acu4 = acu4 + total4
        print('entro aqui')
    elif (edad > 65):
        asiento = 5000
        descuento5 = asiento * 0.25
        total5 = asiento - descuento5
        acu5 = acu5 + total5
        print('entro aqui')
    i = int(input('¿Desea continuar? (1).SI (2).NO : '))
    

print('total de descuento para el rango de edades entre 5 - 14 años es: ',total1)
print('total de descuento para el rango de edades entre 15 - 19 años es: ',total2)
print('total de descuento para el rango de edades entre 20 - 45 años es: ',total3)
print('total de descuento para el rango de edades entre 46 - 65 años es: ',total4)
print('total de descuento para el rango de edade de 65 años en adelante: ',total5)

# =============================================================================
# Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
# siguiente tabla:
# Valor vendido Comisión
# Menor o igual que 20
# Millones
# 10%
# Mayor de 20 Millones y
# menor de 40 Millones
# 15%
# Mayor o igual de 40 20%
# Millones y menor de 80
# Millones
# Mayor o igual de 80
# millones y menor de
# 160 Millones
# 25%
# De 160 Millones en
# adelante
# 30%
# Realice un método que diga cuanto vendió y la comisión de los 100
# vendedores que tiene la empresa.
# =============================================================================

def cone():
    acu1 = 0
    acu2 = 0
    acu3 = 0
    acu4 = 0
    acu5 = 0
    venta1 = 0
    venta2 = 0
    venta3 = 0
    venta4 = 0
    venta5 = 0
    for i in range(100):        
        valor = int(input(f'Ingrese valor anual vendido por el vendedor N°{i + 1}: '))
        if (valor <= 20000000):
            comision = valor * 0.10
            venta1 = venta1 + valor
            acu1 = acu1 + comision                 
        elif (valor > 20000000 and valor < 40000000):
            comision = valor * 0.15
            acu2 = acu2 + comision
            venta2 = venta2 + valor                
        elif (valor >= 40000000 and valor < 80000000):
            comision = valor * 0.20
            acu3 = acu3 + comision
            venta3 = venta3 + valor                 
        elif (valor >= 80000000 and valor < 1600000000):
            comision = valor * 0.25
            acu4 = acu4 + comision
            venta4 = venta4 + valor
        elif (valor > 1600000000):
            comision = valor * 0.30
            acu5 = acu5 + comision
            venta5 = venta5 + valor
                     
    total = venta1 + venta2 + venta3 + venta4 + venta5
    comisionTotal = acu1 + acu2 + acu3 + acu4 + acu5
    print('El total vendido es: ',total)
    print('Total de comision es: ',comisionTotal)       

# =============================================================================
# 10. La empresa Encuestas S.A desea crear una función que les permita
# conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
# el ganador o indicar si hubo empate y la cantidad de votos obtenidos.
# =============================================================================
def votos():
    votos1 = 0
    votos2 = 0
    votos3 = 0
    cantidato1 = ""
    candidato2 = ""
    candidato3 = ""

    candidato1 = input('Ingrese el nombre del candidato N°1: ')
    votos1 = int(input('Ingresar cantidad de votos del candidato N°1: '))
    
    candidato2 = input('Ingrese el nombre del candidato N°2: ')
    votos2 = int(input('Ingresar cantidad de votos del candidato N°2: '))
    
    
    candidato3 = input('Ingrese el nombre del candidato N°3: ')
    votos3 = int(input('Ingresar cantidad de votos del candidato N°3: '))
        
    
    if (votos1 > votos2 and votos1 > votos3):
        print(f'El ganador es : {candidato1}')
        
    if (votos2 > votos1 and votos2 > votos3):
        print(f'El ganador es : {candidato2}')
        
    if (votos3 > votos1 and votos3 > votos2):
        print(f'El ganador es : {candidato3}')
        
    if (votos1 == votos2):
        print(f'Hay un empate!! entre: {candidato1} y candidato {candidato2}')
        
    if (votos1 == votos3):
        print(f'Hay un empate!! entre: {candidato1} y candidato {candidato3}')
        
        
    if (votos2 == votos3):
        print(f'Hay un empate!! entre: {candidato2} y candidato {candidato3}')
        
        
    if (votos3 == votos1):
        print(f'Hay un empate!! entre: {candidato3} y candidato {candidato1}')
        
    if (votos3 == votos2):
        print(f'Hay un empate!! entre: {candidato3} y candidato {candidato2}')