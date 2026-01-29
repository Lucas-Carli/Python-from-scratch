"""
3) REGISTRARSE EN UNIVERSIDAD. Realizar un programa que le pida al 
usuario que ingrese su edad (recordar el comando input y que siempre es 
un string) , en el caso de que su edad sea menor a 18 o mayor a 80, 
imprimir que no puede registrarse en la universidad, caso contrario, 
imprimir que sí puede registrarse. 
"""

# operadores de comparación 
# operadores condicionales
# operadores lógicos

# input
edad = int(input("Ingrese su edad: "))

# camino y output
if edad < 18 or edad > 80:
    print("No puede registrarse en la universidad")
else: 
    print("Puede proceder a registrarse")