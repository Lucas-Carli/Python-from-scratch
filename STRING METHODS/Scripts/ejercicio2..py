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

# input

texto = input("ingrese un texto por teclado dejando un espacio en blanco entre cada palabra, coloque un punto cuando finalice el texto: \n ")
palabras = []
# proceso
## separar el texto en un array de palabras
palabras = texto.split(" ")
print(palabras)
## crear un contador para palabras de 3, 5 y 7 letras 
tres_letras = 0
cinco_letras = 0
siete_letras = 0
## crear contador de palabras con más de 3 letras, que la tercera letra sea vocal
tercera_vocal = 0


### Falta esto 

## Crear un contador para palabras que tengan solo 1 o 2 vocales en total
una_o_dos_vocales = 0
#### Calcular el porcentaje de estas palabras sobre el total
# Crear contador para palabras que contengan más de una vez la silaba 'pe'
mas_dos_veces_pe = 0
vocal = 0

for palabra in palabras:
    if palabra[len(palabra)-1] == ".":
        palabra = palabra.replace(".", "")  
    # Si tiene 2 vocales 
    for letra in palabra:
        if letra.lower() in "aeiou":
            vocal += 1

            if vocal > 2:
                break
    if vocal == 1 or vocal == 2:
        una_o_dos_vocales += 1  

    # Reiniciar vocales 
    vocal = 0

    # Si tiene 2 silabas ‘pe’
    if palabra.count("pe") > 1:
        mas_dos_veces_pe += 1
    # Si tiene 3 letras
    if len(palabra) == 3:
        tres_letras += 1
    # Si tiene mas de 3 letras 
    elif len(palabra) > 3:
    # si tiene 5 letras
        if len(palabra) == 5:
            cinco_letras += 1
    # si tiene 7 letras 
        if len(palabra) == 7:
            siete_letras += 1
    # si la tercera es vocal 
        if palabra[2].lower() in "aeiou":
            tercera_vocal += 1

# ================== OUTPUT ==================

print("\nRESULTADOS")
print("-" * 40)

# A)
print("A) Palabras con 3 letras:", tres_letras)
print("   Palabras con 5 letras:", cinco_letras)
print("   Palabras con 7 letras:", siete_letras)

# B)
print("\nB) Palabras con más de 3 letras y tercera letra vocal:", tercera_vocal)

# C)
total_palabras = len(palabras)

if total_palabras > 0:
    porcentaje = (una_o_dos_vocales * 100) / total_palabras
else:
    porcentaje = 0

print("\nC) Porcentaje de palabras con 1 o 2 vocales:", porcentaje, "%")

# D)
print("\nD) Palabras que contienen más de una vez la sílaba 'pe':", mas_dos_veces_pe)

print("-" * 40)

# output
# a) Mostrar cuantas palabras tiene 3, 5 y 7 letras
# b/ Mostrar cuantas palabras tienen más de 3 letras y su tercer letra es vocal
# c) Mostrar que porcentaje de palabras tienen solo una o dos vocales 
# d) mostrar cuantas palabras tienen más de una vez la sílaba 'pe'        if palabra[2].lower == "a" or palabra[2].lower == "e" or palabra[2].lower == "i" or palabra[2].lower == "o" or palabra[2].lower == "u":
