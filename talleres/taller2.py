# TALLER 2 - EJERCICIOS DE ALGORITMIA ESTRUCTURA CONDICIONAL



#Ejercicio1

try:
    num1 = (float(input("por favor digite el primer numero: ")))
    num2 = (float(input("por favor digite el segundo numero: ")))

    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
except:
    print("error por favor digita numeros y no letras")


'''
num1 = (float(input("por favor digite el primer numero: ")))
num2 = (float(input("por favor digite el segundo numero: ")))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

'''

#Ejercicio4

try:
    tiempo = float(input("cuantos minutos duro tu llamada: "))

    if tiempo <= 3:
        print("debes pagar 200 pesos")
    else:
        valorMas = tiempo - 3
        valorTotal = (valorMas * 100) + 200
        print(f"el valor a pagar es {valorTotal} pesos")
except:
    print("por favor digite numeros no letras")

'''
tiempo = float(input("cuantos minutos duro tu llamada: "))

if tiempo <= 3:
    print("debes pagar 200 pesos")
else:
    valorMas = tiempo - 3
    valorTotal = (valorMas * 100) + 200
    print(f"el valor a pagar es {valorTotal} pesos")

'''

#Ejercicio5
'''
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
        totalConDes = descuento * cantidad
        print(f"el nombre del producto es {articulo}, su clave es {clave}, su precio original es {precio} por cada uno de los articulos y el producto con descuento por la clave escogida es {descuento} y en total seria {totalConDes}")
    else:
        descuento = precio - (0.20*precio)
        totalConDes = descuento * cantidad
        print(f"el nombre del producto es {articulo}, su clave es {clave}, su precio original es {precio} por cada uno de los articulos y el producto con descuento por la clave escogida es {descuento} y en total seria {totalConDes}")
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




#Ejercicio 2

num = int(input("por favor digita un numero entre 1 y 10: "))

 

if num >= 1 and num <= 10:
    if ((num % 2) == 0):
        numIs = "es par"
    else:
        numIs = "es impar"
    match numIs:
        case "es impar":
            print("numero impar")
        case "es par":
            print("numero par")
else:
    print("numero invalido")


#Ejercicio 3

num = int(input("ingrese un valor de 1 a 10: "))

if num >= 1 and num <= 10:
    match num:
        case 1:
            print(f"{num} uno")
        case 2:
            print(f"{num} dos")
        case 3:
            print(f"{num} tres")
        case 4:
            print(f"{num} cuatro")
        case 5:
            print(f"{num} cinco")
        case 6:
            print(f"{num} seis")
        case 7:
            print(f"{num} siete")
        case 8:
            print(f"{num} ocho")
        case 9:
            print(f"{num} nueve")
        case 10:
            print(f"{num} dies")
else:
    print("numero invalido")


'''