# TALLER 2 - EJERCICIOS DE ALGORITMIA ESTRUCTURA CONDICIONAL

#Ejercicio1

num1 = (float(input("por favor digite el primer numero: ")))
num2 = (float(input("por favor digite el segundo numero: ")))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

#Ejercicio4

tiempo = float(input("cuantos minutos duro tu llamada: "))

if tiempo <= 3:
    print("debes pagar 200 pesos")
else:
    valorMas = tiempo - 3
    valorTotal = (valorMas * 100) + 200
    print(f"el valor a pagar es {valorTotal} pesos")

#Ejercicio5

N = int(input("cuantos conejos hay en total: "))
C1 = int(input("cuantos conejos blancos hay en total: "))
C2 = int(input("cuantos conejos negros hay en total: "))

print("----------------------------------------------")


if ((C1 or C2) > N) or (C1 + C2) > N:
    print("error sumaste mas conejos del total ")
else:
    x = int(input("cuantos conejos negros se vendieron? "))
    y = int(input("cuantos conejos blancos se vendieron? "))
    xyVendido = x + y
    print(f"se vendieron {xyVendido} de {N}")

    P1 = float(input("cuanto vale el conejo blanco? "))
    P2 = float(input("cuanto vale el conejo negro? "))

    totalBlancos = y * P1
    totalNegros = x * P2

    montoTotal = totalBlancos + totalNegros
    print(f"el valor total de la venta es de {montoTotal} pesos")

    if x > y:
        print(f"se vendieron mas conejos negros que fueron {x} a comparacion de los blancos que fueron {y}")
    else:
        print(f"se vendieron mas conejos blancos que fueron {y} a comparacion de los negros que fueron {x}")



#Ejercicio6



print("a continuacion sumaremos las 3 notas de las evaluaciones...")
eva1 = float(input("cuanto fue tu nota de la primera evaluación? "))
eva2 = float(input("cuanto fue tu nota de la segunda evaluación? "))
eva3 = float(input("cuanto fue tu nota de la tercera evaluación? "))

if (eva1 >= 1 and eva1 <= 5) and (eva2 >= 1 and eva2 <= 5) and (eva3 >= 1 and eva3 <= 5):
    promedioPrevios = (eva1 + eva2 + eva3)/3
    totalPrevios = promedioPrevios * 0.60
    print(f"la nota de previos es {totalPrevios}")
else:
    print("pusiste algun dato mayor a 5 puntos o menor a 1 punto")

print("------------------------------------------------")

print("a continuacion sumaremos las 2 notas de los trabajos...")
trabajo1 = float(input("cuanto fue la nota del trabajo 1? "))
trabajo2 = float(input("cuanto fue la nota del trabajo 2? "))

if (trabajo1 >= 1 and trabajo1 <= 5) and (trabajo2 >= 1 and trabajo2 <= 5):
    promedioTrabajos = (trabajo1 + trabajo2)/2
    totalTrabajos = promedioTrabajos * 0.40
    print(f"la nota de trabajos es {totalTrabajos}")

    notaFinal = totalTrabajos + totalPrevios
    print(f"la nota final es {notaFinal}")
else:
    print("pusiste algun dato mayor a 5 puntos o menor a 1 punto")



#Ejercicio7



articulo = input("ingresa el articulo que deseas comprar: ")
clave = int(input("ingrese la clave del producto este puede ser 1 o 2: "))



if clave == 1 or clave == 2:
    precio = float(input("ingresa el valor del producto: "))
    cantidad = int(input("ingrese la cantidad a comprar: "))
    if clave == 1:
        descuento = precio - (0.10*precio)
        print(f"el nombre del producto es {articulo}, su clave es {clave}, su precio es original es {precio} y su valor con descuento es {descuento}")
    else:
        descuento = precio - (0.20*precio)
        print(f"el nombre del producto es {articulo}, su clave es {clave}, su precio es original es {precio} y su valor con descuento es {descuento}")
else:
    print("la clave del producto debe ser igual a 1 o 2 para seguir")



#Ejercicio 8



presupuestoAnual = float(input("cuanto es el presupuesto anual: "))

porcentajePsiquiatria = float(input("que porcentaje le toca al departamento de psiquiatria: "))
totalPsiquiatria = presupuestoAnual * (porcentajePsiquiatria/100)

porcentajePediatria = float(input("que porcentaje le toca al departamento de pediatria: "))
totalPediatria = presupuestoAnual * (porcentajePediatria/100)

porcentajeTraumotologia = float(input("que porcentaje le toca al departamento de traumotologia: "))
totalTraumotologia = presupuestoAnual * (porcentajeTraumotologia/100)

if (totalPsiquiatria + totalPediatria + totalTraumotologia) > presupuestoAnual:
    print("error sumaste demas en los porcentajes del presupuesto para los departamentos")
else:
    print(f"el porcentaje para psiquiatria es {totalPsiquiatria}, pediatria {totalPediatria}, traumotologia {totalTraumotologia}")


#ejercicio 9



distancia = float(input("por favor ingrese la distancia (kilometros) a recorrer: "))

dias = int(input("por favor ingrese el numero dias de estancia en tu destino: "))

total = 2.5 * distancia

if (dias >= 7 and distancia > 800):
    descuento = total - (0.30 * total)
    print(f"el valor total de su ticket es {descuento} dolares")
else:
    print(f"el total de su ticket es {total} dolares")

