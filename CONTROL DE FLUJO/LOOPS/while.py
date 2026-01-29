"""
while condicion:
    bloque de instrucciones
"""

x = 0

while x < 10:
    x += 1
    print(x)
    if x == 3:
        print("no me gusta el número 3")
        break

print("Fin")