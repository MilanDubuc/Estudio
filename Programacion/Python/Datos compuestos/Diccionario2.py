diccionario = {
    # "Clave/Key"       : Dato
    "nombre"            : "pedro",
    "apellido"          : "perez",
    "dni"               : 12345234,
    "talle"             : 30 
}

# tambien se puede:

diccionario = dict(
    # clave = Dato
    nombre='pedro', 
    apellido='perez', 
    dni=12345234, 
    talle=30
)

#tambien se puede usar como key datos hasheables:

diccionario = {
    # clave = Dato
    ("nombre", "apellido"):['pedro', 'perez'], #tupla
    "dni":12345234, 
    "talle":30
}

print(diccionario["nombre", "apellido"])

#dict.fromkeys([Lista de keys], Dato) : crea un diccionario con todas las keys igual al dato.

diccionario = dict.fromkeys(["nombre", "apellido", "dni", "talle"])

print(diccionario)


