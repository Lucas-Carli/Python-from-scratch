"""
Escribe una calculadora de liquidación: para calcular la liquidación,
el cálculo es muyy sencillo. Deberás dividir tu salario bruto en 30 y luego
multiplicarlo por los días trabajados en tu último mes. El programa debe: 
A. Contener una variable que refiera el salario_bruto, y que tenga como valor un monto (Integer o float).
B. Contener una variable de días trabajados, que tenga como valor un número entero.
C. Dividr la variable salario_bruto en 30, y ese resultado multiplicarlo por los días trabajados.
Imprimir por pantalla el resultado final.
"""

# inputs
salarioBruto = 200000  # ejemplo de salario bruto
diasTrabajados = 15  # ejemplo de días trabajados
# camino
salarioPorDia = salarioBruto / 30
liquidacion = salarioPorDia * diasTrabajados

# outputs
print("La liquidación es de:", str(liquidacion))
