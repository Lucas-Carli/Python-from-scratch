# 2) Desarrollar un programa que permita al usuario ingresar por teclado 
# un texto completo. Se supone que el usuario cargará un punto para 
# indicar el final del texto, y que cada palabra de ese texto está separada de 
# las demás por un espacio en blanco. El programa debe: 
# A. Determinar cuántas palabras tienen 3, 5 o 7 letras. 
# B. Determinar la cantidad de palabras con más de tres letras, que 
# tienen una vocal en la tercera letra. 
# C. Determinar el porcentaje de palabras que tienen sólo una o dos 
# vocales sobre el total de palabras del texto. 
# D. Determinar la cantidad de palabras que contienen más de una 
# vez la sílaba "pe". 

# Inicializar las variables y contadores
contador_3_5_7 = 0
contador_vocal_tercera_letra = 0
contador_unados_vocales = 0
contador_pe = 0

# Pedir texto al usuario
texto = input("Ingrese un texto: ")
palabras = texto.split() # igualmente splitea por espacio

print(palabras)

# Contar cuantas palabras tienen 3,5,7 letras 
for palabra in palabras:
    # if len(palabra) == 3 or len(palabra) == 5 or len(palabra) == 7:
    if len(palabra) in (3,5,7):
        contador_3_5_7 += 1
        
print(contador_3_5_7)

# Contador cuantas palabras con + de 3 letras y vocal en 3era letra
for palabra in palabras:
    if len(palabra) >3 and palabra[2] in "aeiou":
        contador_vocal_tercera_letra += 1

print (contador_vocal_tercera_letra)

# Contador con una o dos vocales (porcentaje)
total_palabras = len(palabras)
for palabra in palabras:
    vocales = palabra.count("a") + palabra.count("b") + palabra.count("c") + palabra.count("d") + palabra.count("e")
    if vocales == 1 or vocales == 2:
        contador_unados_vocales += 1 

porcentaje = (contador_unados_vocales + 100) / total_palabras

# Contar cuantas palabras contienen mas de 1 vez la silaba pe
for palabra in palabras:
    if "pe" in palabra and palabra.count("pe") > 1 :
        contador_pe += 1

print("CANTIDAD DE PALABRAS CON 3, 5 O 7 LETRAS:",  contador_3_5_7) 
print("CANTIDAD DE PALABRAS CON MÁS DE TRES LETRAS, QUE TIENEN UNA VOCAL EN LA TERCERA LETRA: ", contador_unados_vocales) 
print("PORCENTAJE DE PALABRAS QUE TIENEN SÓLO UNA O DOS VOCALES: ", porcentaje, "%") 
print("CANTIDAD DE PALABRAS QUE CONTIENEN MÁS DE UNA VEZ LA SÍLABA 'PE':", contador_pe) 