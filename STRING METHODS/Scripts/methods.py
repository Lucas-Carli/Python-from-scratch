## REPLACE -> reemplazar -> reemplazar ciertos caracteres por otros 

nombre = "PENSAR"
print(nombre.replace("A","11111"))

texto = "bjsdk f      gregverg     grg"
print(texto)
texto = texto.replace(" ", "")
print(texto)


# SPLIT -> separa y me devuelve una lista ocns los strings separados
nombre = "Lucas Milo Carli"
print(nombre.split(" "))

url = "https://www.1lugarparapensar/Python/curso"
print(url.split("/"))

texto = "Lucas,25,Rosario"
print(texto.split(","))

# strip() -> remover los espacios que queden al inicio y al final del str
texto = "       hola dsdwd    "
print(texto.strip())

# swapcase() -> Intercambiar la mayuscula/minuscula de nuestro string
nombre = "PensaR curso"
print(nombre.swapcase())

# title() ->  Poner el string en modo titulo
print(nombre.title())

# upper() -> Pasar todo a mayusucla
nombre = "PensaR curso"
print(nombre.upper())

# lower() -> Pasar todo a minuscula
nombre = "PensaR curso"
print(nombre.lower())

# find() -> encontrar ciertos caracteres en mi string y me devuelve el índice
print(nombre.find("curso"))

# count() -> contar la cantidad de veces que aparecen ciertos caracteres en mi string
print(nombre.count("curso"))

# len() -> devolver la longitud de mi string
print(len(nombre))


# indexar
nombre = "PENSAR"
print(nombre[1])

# slicing
nombre = "PENSAR"
print(nombre[1:3])

# secuencia de escape 
texto = "Hola como estás\n mi nombre es Lucas\tCarli"
print(texto)

