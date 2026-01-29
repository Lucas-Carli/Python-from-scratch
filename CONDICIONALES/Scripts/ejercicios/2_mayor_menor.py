"""
2) Escribe un programa para calcular el más grande de dos números 
ingresados por el usuario. 
"""

# Operadores matemáticos (%), operadores de comparación 
# y condicionales

# input
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

# camino y output
if numero1 > numero2:
    print("El número mayor es {}".format(numero1))
elif numero1 < numero2 :
    print("El número mayor es {}".format(numero2))
else: 
    print("Los números son iguales")
