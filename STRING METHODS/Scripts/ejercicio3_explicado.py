# 3) Hacer el juego del Ahorcado. Usa While y Condicionales. 

# Inicializar variables
palabra_adivinar = "perro"
letras_acertadas = 0
intentos = 0
permitidos = 10

print("¡Bienvenido al juego del ahorcado!")
print(f"La palabra a adivinar contiene {len(palabra_adivinar)} letras.")
print(f"Tiene ", permitidos, " intentos!")

while intentos < permitidos and letras_acertadas < len(palabra_adivinar):
    letra = input("Ingrese una letra: ")
    if len(letra)>1:
        print("Solo se permite una sola letra.")
        continue
    intentos += 1
    if letra in palabra_adivinar:
        print("Correcto! la letrá está acertada")
        contador = palabra_adivinar.count(letra)
        letras_acertadas += contador
    else: 
        print("Incorrecta, la letra no se encuentra en la palabra")

print("El juego ha terminado!")
if letras_acertadas == len(palabra_adivinar):
    print(f"Felicidades has ganado el juego con un total de {letras_acertadas} aciertos")
