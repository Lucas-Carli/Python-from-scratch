# 4) Programa para invitar un máximo de 10 personas a una fiesta (usar 
# range y for). 

maximo = 3 
invitados = ""

for invitado in range(0, maximo):
    nombre = input("Ingrese el nombre y el apellido de su invitado: ")
    if invitado == (maximo - 1):
        invitados += f" y {nombre} ."
    else:
        invitados += f"{nombre} , "

print(f"Los invitados son: {invitados}")

if 22 %2 == 0:
    print()

