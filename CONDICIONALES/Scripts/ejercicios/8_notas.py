"""
8) Escriba un programa para solicitar una puntuación entre 0 y 10. Si la 
puntuación está fuera de rango, imprime un error. Si el puntaje está entre 
0 y 10, imprima una calificación usando la siguiente tabla: 
Nota numérica
>= 9
>=8
Nota en letras
A
B
>=7
C
>=6
D
< 6
F
"""

# nota = int(input("Ingrese la nota entre 0 y 10: "))

# if nota >= 9 and nota < 11: 
#     print("Su nota es A")
# elif nota >= 8: 
#     print("Su nota es B")
# elif nota >= 7: 
#     print("Su nota es C")
# elif nota >= 6: 
#     print("Su nota es D")
# elif nota < 6 and nota <= 0: 
#     print("Su nota es F")
# else:
#     print("El nota ingresado está fuera del rango")

nota = int(input("Ingrese la nota entre 0 y 10: "))
nota_permitida = range(1,11)

if nota in nota_permitida:
    if nota >= 9:
        print("Su nota es A")
    elif nota == 8: 
        print("Su nota es B")
    elif nota == 7: 
        print("Su nota es C")
    elif nota == 6: 
        print("Su nota es D")
    else:  
        print("Su nota es F")
else:
    print("El nota ingresado está fuera del rango")