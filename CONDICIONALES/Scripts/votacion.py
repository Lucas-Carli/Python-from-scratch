"""
IF condicion1:
    instrucciones
ELIF condicion2:
    otras instrucciones
ELSE:
    otras instrucciones
"""

#solo una condicion puede ser verdadera y va a ser ejecutado
#en caso de ninguno ser verdadero, se ejecutará el else

edad = int(input("¿Cuál es su edad?"))

if edad < 16: 
    print("No eres mayor de edad y no puedes votar")
elif edad >= 16 and edad < 18:
    print("No eres mayor de edad pero puedes votar")
else:
    print("Eres mayor de edad y tienes obligación de ir a votar") 


