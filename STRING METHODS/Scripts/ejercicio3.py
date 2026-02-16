# 3) Hacer el juego del Ahorcado. Usa While y Condicionales. 

# Jugador 1 ingresa una palabra:
palabra = input("Jugardor 1 ingrese una palabra y presione enter: ")
# palabra = "guitarra"
print("La palabra a adivinar tiene ", len(palabra), " letras ")

palabra_por_adivinar = ["_"] * len(palabra)
print(" ".join(palabra_por_adivinar))
ganador = False

while ganador == False:

    letra = input("Ingrese una letra ")

    if letra in palabra:
        for indice, caracter in enumerate(palabra):
            if caracter == letra:
                palabra_por_adivinar[indice] = letra

        print(" ".join(palabra_por_adivinar))

    else:
        print("Letra incorrecta")

    if "_" not in palabra_por_adivinar:
        ganador = True
        print("Ganaste!")






