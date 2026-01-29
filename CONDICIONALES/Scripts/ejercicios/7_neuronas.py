"""
7) SINAPSIS DE NEURONAS. Un potencial de acción se genera cuando 
un estímulo cambia el potencial de membrana alcanzando o superando el 
umbral de excitación. El umbral a menudo se ubica entre los -50 a -55 mV. 
Es importante mencionar que el potencial de acción obedece a lo que 
conocemos como ley del todo o nada. Esto significa que cualquier 
estímulo por debajo del umbral no provocará reacción alguna, mientras 
que estímulos que alcancen o superen el umbral generarán una respuesta 
completa en la célula excitable. Dado que al potencial fuera de la célula 
se le asigna por convención un valor igual a cero, el potencial de reposo 
(VR) es negativo. El valor normal es de - 60 mV. Haga un programa que 
permita al usuario agregar un input de voltios de excitación y devuelva si 
la neurona llegó al umbral o no.
"""
#input
voltios = int(input("Ingrese la cantidad de voltios: "))
potencial_reposo = -60
umbral_excitacion = range(-55, -50)

if potencial_reposo + voltios in umbral_excitacion:
    print("La neurona llegó al umbral de excitación")
else: 
    print("La neurona no ha llegado al umbral de excitación")

