"""
Yo quiero ahorrar dinero
El pgroama me va a preguntar cuanto quiero ahorrar 
y luego me va a preguntar cuanto ahorro hasya que llegue al objetivo
"""

objetivo = float(input("¿Cuánto dinero queres ahorrar?"))
ahorrado = 0
fin = False

while ahorrado < objetivo and fin != True:
    cantidad_a_agregar = float(input("Indica cuántos euros queres guardar: "))
    ahorrado += cantidad_a_agregar
    if cantidad_a_agregar == 11:
        fin = True

print("Has llegado a tu objetivo! FELICITACIONES")