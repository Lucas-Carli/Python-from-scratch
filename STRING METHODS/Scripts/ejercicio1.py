# 1) Escriba un programa en el que se pregunta al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra que quiera buscar en la frase: ").lower()

# isalpha() -> va a chequear si el string son todas letras
while not letra.isalpha() or len(letra) > 1:
    print(f"La letra {letra} no es válida")
    letra = input("Ingrese una letra que quiera buscar en la frase: ").lower()

print(frase.count(letra))

