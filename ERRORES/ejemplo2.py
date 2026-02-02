numero = input("Ingrese un numero para dividir: ")
try: # siempre se ejecuta 
    numero_int = int(numero)
    resultado = 100/numero_int
except ValueError: # solo en excepión Value Error
    print("Error: Solo puedes ingresar números " )
except ZeroDivisionError: # solo en excepión Zero Division Error
    print("Error: No se puede dividir por cero " )
else: #solo en exito
    print("Su resultado es: ")
    print(resultado)
finally: # siempre
    print("Finalización del programa")