
nombre = "Marlon"
edad = 15

soltero = True
salario = 1000000

ciudad = "Bucaramanga"
año = 2023
altura = 1.80
graduado = False

'''
print(nombre, edad, soltero, salario)
print(ciudad, año, altura, graduado)

print(f"hola mi nombre es {nombre} y tengo {edad} años, Soltero: {soltero}, graduado: {graduado} tengo {altura} de altura, mi slario es de {salario} de pesos y vivo en {ciudad} en este año {año}")
'''

'''
nombreUsuario = input("cual es tu nombre? ")
edadUsuario = int(input("cual es tu edad? "))
estadoCivilUsuario = bool(input("estas soltero? "))
salarioUsuario = int(input("de cuanto es tu salario? "))
ciudadUsuario = input("en que ciudad vives? ")
añoUsuario = int(input("en que año estas? "))
alturaUsuario = float(input("cual es tu altura? "))
graduadoUsuario = bool(input("estas graduado? "))

print(f"hola mi nombre es {nombreUsuario} y tengo {edadUsuario} años, Soltero: {estadoCivilUsuario}, graduado: {graduadoUsuario} tengo {alturaUsuario} de altura, mi slario es de {salarioUsuario} de pesos y vivo en {ciudadUsuario} en este año {añoUsuario}")
'''

if edad >= 18:
    print("puedes ingresar")
else: 
    print("no puedes entrar")