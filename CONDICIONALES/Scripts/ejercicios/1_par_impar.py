"""
1) Escribe un programa que pida al usuario que ingrese un número. 
Chequear si el numero ingresado es numero par o impar. Imprimir por 
pantalla si es par o impar. 
"""

# Operadores matemáticos (%), operadores de comparación 
# y condicionales

# input
numero = int(input("Ingrese un número: "))

# camino y output
if numero % 2 == 0:
    print("El número {} es par".format(numero))
else:
    print("El número {} es impar".format(numero))