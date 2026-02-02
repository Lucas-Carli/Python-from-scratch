# 3) Ejercicio LOOP WHILE. Escriba un programa que solicite una 
# contraseña (el texto de la contraseña no es importante) y la vuelva a 
# solicitar hasta que las dos contraseñas coincidan. Ejemplo de lo que debe 
# aparecer por consola: 
# CONFIRME SU CONTRASEÑA 
# Escriba su contraseña: holaholachau 
# Escriba de nuevo su contraseña: holachau 
# Las contraseñas no coinciden. Inténtelo de nuevo. 
# Escriba su contraseña: holaholachau 
# Escriba de nuevo su contraseña: holaholachau 
# Contraseña confirmada. ¡Hasta la vista! 

# contraseña1 = ("1")
# contraseña2 = ("2")

# print("CONFIRME SU CONTRASEÑA") 

# while contraseña1 :
#     contraseña1 = input("Escriba su contraseña: ")
#     contraseña2 = input("Escriba de nuevo su contraseña: ")
#     if contraseña1 == contraseña2: 
#         print("Contraseña confirmada. ¡Hasta la vista!")
#         break
#     print("Las contraseñas no coinciden: Inténtelo nuevamente! ")
    
print("CONFIRME SU CONTRASEÑA") 

while True:
     contraseña1 = input("Escriba su contraseña: ")
     contraseña2 = input("Escriba de nuevo su contraseña: ")
     if contraseña1 == contraseña2:
        print("Contraseña confirmada. ¡Hasta la vista!")
        break
     else:
        print("Las contraseñas no coinciden: Inténtelo nuevamente! ")
          
