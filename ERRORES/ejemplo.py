numero = input("Ingrese un numero para dividir: ")
try: # siempre se ejecuta 
    numero_int = int(numero)
    resultado = 100/numero_int
except Exception as e: # solo en excepión
    print("Hubo un error " )
else: #solo en exito
    print("Su resultado es: ")
    print(resultado)
finally: # siempre
    print("Finalización del programa")