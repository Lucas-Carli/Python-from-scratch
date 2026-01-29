"""
IF ANIDADOS

IF condicion:
    if condicion111:
        instrucciones
ELSE: 
    instrucciones
"""

saber_manejar = input("Sabes manejar")
dinero = input("tenes dinero?")
bicicleta = input("tenes bicicleta?")

if saber_manejar == "si" :
    print("Puedes ir en auto")

if dinero == "si":
    print("Puedes ir en bus")

if bicicleta == "si":
    print("Puedes ir en bicicleta")

print("Puedes ir caminando")
