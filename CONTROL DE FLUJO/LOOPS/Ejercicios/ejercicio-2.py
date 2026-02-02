# 2) Seguir una receta para hacer galletas de chocolate. Hay que poner 
# 100ml de leche, 30gramos de harina y 10 gramos de chocolate. Ayudarse 
# del while para hacer esto. En caso de que el usuario se pase con los 
# ingredientes, tirarlos y volver a cero. 

leche = 0
harina = 0
chocolate = 0

while leche < 100 or harina < 30 or chocolate < 10:
        leche += int(input("Sirva leche a la receta por favor: "))
        harina += int(input("Sirva harina a la receta por favor: "))
        chocolate += int(input("Sirva chocolate a la receta por favor: "))

        if leche > 100 or harina > 30 or chocolate > 10:
            print("Te has excedido con los ingredientes, empieza de nuevo. ")
            leche = 0
            harina = 0 
            chocolate = 0

print("Felicidades, podrás comer tus galletas en 30 minutos")

 
