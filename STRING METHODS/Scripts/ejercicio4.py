# 4) Un conocido portal de empleo requiere un programa para validar las 
# búsquedas que se cargan en su página. Por cada búsqueda se requiere: 
# • CUIT: validar que sea un texto compuesto por 13 números separados 
# por guiones de la siguiente manera: 00-00000000-0. 
# • Descripción de la búsqueda: un texto donde cada palabra se separa 
# con un espacio y termina con punto. Debe tener un máximo de 60 
# caracteres y un mínimo de 3 palabras. 
# • Salario ofrecido: controlar que sea un valor mayor a 0 
# Si todos los datos son válidos, mostrar el aviso completo. En caso 
# contrario, informar que no es posible mostrarlo.


# Validar cuit
cuit_valido = ""
descripcion_valido = ""
salario_valido_valido = ""

cuit = input("Ingrese CUIT de su empresa: ")
if len(cuit) == 13 and cuit[2] == "-" and cuit[11] == "-"  and cuit[:2].isdigit() and cuit[3:11].isdigit() and cuit[12].isdigit():
    cuit_valido = cuit
    print("El CUIT es válido")
else:
    print("cuit no es válido")

# Validar texto
#   minimo 3 palabras
#   maximo 60 caracteres 
#   cada palabra debe estar separada por un espacio entre si
#   el texto termina en punto
descripcion = input("Ingrese una descripción válida: ")
if len(descripcion) > 60:
    print("La descripción tiene más de 60 caracteres")
elif not descripcion.endswith("."):
    print("La descripcion tiene que terminar en punto")
elif len(descripcion.split()) < 3:
    print("La descripcion tiene que tener 3 palabras como mínimo") 
else: 
    print("La descripción es válida")
    descripcion_valido = descripcion

# validar salario
#   debe ser mayor a cero
salario = int(input("Ingrese el salario ofrecido: "))
if salario <= 0:
    print("El salario ofrecido tiene que ser mayor a cero")
else: 
    print("El salario es válido")
    salario_valido = salario

# Si los datos son validos 
#   Armar un aviso y mostrar por pantalla
# sino
#   Mostrar mensaje "No es posible emitir aviso"    
if cuit_valido == cuit and descripcion_valido == descripcion and salario_valido == salario: 
    print("\n" + "=" * 50)
    print("           AVISO DE EMPLEO PUBLICADO")
    print("=" * 50)
    print(f"CUIT Empresa: {cuit}")
    print(f"Descripción del puesto: {descripcion}")
    print(f"Salario ofrecido: ${salario:,.2f}")
    print("=" * 50)
    print("El aviso ha sido validado y publicado correctamente.")
    print("=" * 50)
else:
    print("No es posible emitir aviso")

