"""
Un avión viaja 395000 metros en 9000 segundos.
Escribe un programa para calcular la velocidad del avión (velocidad = distancia / tiempo).
"""

# inputs
distancia = 395000  # en metros
tiempo = 9000      # en segundos    
tiempoEnHoras = tiempo / 3600  # convertir segundos a horas

# camino
velocidad = distancia / tiempo  # en metros por segundo
velocidadEnHoras = distancia / tiempoEnHoras  # en metros por segundo

# output
print("La velocidad del avión es:", velocidad, "metros por segundo")
print("La velocidad del avión es:", velocidadEnHoras, "metros por hora")