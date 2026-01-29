"""
FOR elemento in SECUENCIA:
    bloque de instrucciones
"""

# nombre = "PENSAR"
# for letra in nombre: 
#     print(letra)

# rango = range(0,101,10)
# print (rango)
# for numero in rango:
#     print(numero)

# # calculadora del 1 al 10
# rango = range(1,11)

# numero = int(input("¿Qué número queres multiplicar: ?"))

# for num in rango: 
#     print(f"{numero}*{num} -> {numero*num}")

# calucaldora V2.0
print("--------CALCULADORA V2.0--------")
numeros_a_multiplicar = range(1,11)
multiplicadores = range(1,11)

for numero in numeros_a_multiplicar:
    #tabla
    print(f"--------TABLA DEL {numero}:")
    for mult in multiplicadores:
        print(f"{numero}*{mult} ---> {numero*mult}")
