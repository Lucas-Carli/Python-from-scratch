"""
9) 
Escriba un programa para leer el valor de magnitud de Richter del 
usuario y muestre el resultado de las siguientes condiciones usando la 
estructura if…elif...else.
"""

value = float(input("Enter the value: " ))

if value > 1 and value < 2:
    print("Microearthquakes not felt or rarely felt")
elif value > 2 and value < 4:
    print("Very rarely causes damage")
elif value > 4 and value < 5:
    print("Damage done to weak buildings")
elif value > 5 and value < 6:
    print("Cause damage to the poorly constructed building")
elif value > 6 and value < 7:
    print("Causes damage to well-built structures")
elif value > 7 and value < 8:
    print("Causes damage to most buildings")
elif value > 8 and value < 9:
    print("Causes major destruction")
elif value == 9:
    print("Causes unbelievable damage")
else: 
    print("Error")

