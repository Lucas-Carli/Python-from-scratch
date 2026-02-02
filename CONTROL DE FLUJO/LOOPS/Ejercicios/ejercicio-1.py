# 1) Escriba un programa que pregunte cuántos números se van a 
# introducir, pida esos números, y diga al final cuántos han sido pares y 
# cuántos impares. 

numeros_a_chequear = int(input("Cuántos números vas a ingresar? "))

contador_numeros = 0
contador_pares = int()
contador_impares = int()

while contador_numeros < numeros_a_chequear:
    numero = int(input("Ingrese un número "))
    if numero %2 == 0:
        print(f"{numero} es par" )
        contador_pares += 1
    else: 
        print(f"{numero} es impar" )
        contador_impares += 1

    contador_numeros += 1

print(f"Hay {numeros_a_chequear} números en total, hay {contador_pares} pares y {contador_impares} impares.")
