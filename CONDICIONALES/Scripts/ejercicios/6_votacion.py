"""
6) PROGRAMA PARA VOTAR. Realizar un programa que le pida al usuario 
que ingrese su edad y su nacionalidad. Realizar los siguientes chequeos. 
• Si tiene 18 o más años, es mayor de edad y es obligatorio votar. 
•            Si tiene 16 o 17 años, no es mayor de edad pero es 
opcional votar. 
•            Si tiene menos de 16 años, no puede votar. 
•            Si es Argentino, puede votar. 
•            Si no es Argentino pero tiene ciudadanía, puede votar. 
•            Si no es Argentino y no tiene ciudadania, no puede votar. 
Tener en cuenta ambas condiciones, nacionalidad y edad, para 
determinar si la persona puede votar o no. El programa debe indicar, según 
la edad y la nacionalidad, si la persona puede votar o no.
"""

edad = int(input("Ingrese su edad: "))
pais = input("Es usted argentino o tiene ciudadania argentina? si/no ")

if edad >= 18 and pais == "si": 
    print("Para usted es obligatorio votar.")
elif edad  >= 16 and edad < 18 and pais == "si":
    print("Puedes votar, pero no es obligatorio")
elif edad < 16 and pais == "si":
    print("No puedes votar por minoria de edad")
else: 
    print("No puedes votar porque eres argentino ni tienes ciudadanía. Viva Diegote!!!")

