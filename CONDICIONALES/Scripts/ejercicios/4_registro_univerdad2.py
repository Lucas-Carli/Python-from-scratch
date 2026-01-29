"""
4) REGISTRARSE EN UNIVERSIDAD PARTE 2 (continuación). Si el usuario 
tiene entre 18 y 80 años, le vamos a pedir al usuario que ingrese si tiene 
terminados sus estudios secundarios, en caso de que ingrese "si" imprimir 
"Okey puede registrarse en universidad" ; caso contrario imprimir "No 
puede registrarse”
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
    # a partir de aquí, condicionales anidados
    estudios = input("Tiene estudios secundarios? si/no ")
    if estudios == "si" or estudios == "Si" or estudios == "SI":
        print("Okey puede registrarse en universidad")
    elif estudios == "no" or estudios == "No" or estudios == "NO":
        print("No puede registrarse")
    else:
        print("Lo sentimos, no comprendimos su respuesta, intente nuevamente")