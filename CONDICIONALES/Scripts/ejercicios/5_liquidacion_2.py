"""
5) Calculadora de liquidación PARTE 2 (continuación):  Vamos a 
complicar un poco las cosas. Ahora vamos a evaluar lo que sucede 
cuando despiden a alguien y deben darle, además de la liquidación 
normal (la que programaste antes), una indemnización. A la liquidación, 
hay que sumarle UN MES de sueldo bruto por año trabajado (a partir del 
año de antigüedad, cuenta como 1 año más si se superan los 3 meses). 
Es decir, si trabajas 1 año y 4 meses, cuenta como dos años, por lo tanto 2 
sueldos brutos. Si trabajas 2 años y 6 meses, cuenta como 3 años… y así. 
Por lo tanto, calculemos la indemnización. Para esto necesitamos 
cantidad años trabajando de la persona. Sé original y pensá como podes 
pedirle la antigüedad para luego evaluar su indemnización, teniendo en 
cuenta esto de los 3 meses que te comenté recién. 
"""
# inputs
# salarioBruto = 200000  # ejemplo de salario bruto
# diasTrabajados = 15  # ejemplo de días trabajados
# camino

# outputs
sueldoBruto = int(input("Ingrese en números su sueldo bruto mensual: "))
diasTrabajados = int(input("Ingrese los días trabajados: "))
añosTrabajados = int(input("Ingrese cuantos años ha trabajado, cero es válido:  "))
mesesTrabajados = int(input("Ingrese cuando meses ha trabajado el último año, cero es válido: "))
salarioPorDia = sueldoBruto / 30
liquidacion = salarioPorDia * diasTrabajados
print("La liquidación es de:", str(liquidacion))

liquidacionPorAños = int(0)
liquidacionProporcional = int(0)
liquidacionFinal = int(0)

if sueldoBruto == None or añosTrabajados == None or mesesTrabajados == None: 
    print("Le faltan ingresar datos")

liquidacionPorAños = sueldoBruto * añosTrabajados

if mesesTrabajados > 3: 
    liquidacionProporcional = sueldoBruto

liquidacionFinal = liquidacionPorAños + liquidacionProporcional

print(f"Liquidación por años: ${liquidacionPorAños}")
print(f"Liquidación proporcional: ${liquidacionProporcional}")
print(f"Liquidación final: ${liquidacionFinal}")
