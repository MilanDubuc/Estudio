# listas:
lista = ["string", 123, 40.2, True, "string"]
lista[1] = 124
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

# tuplas; la tupla no se puede modificar
tupla = ("string", 123, 40.2, True, "string")
print(tupla[0])
#no se puede hacer:
# tupla[1] = 124 ----> tira error

# conjuntos; es como una lista pero no tiene orden
conjunto = {"string", 123, 40.2, True, "string"}
# el conjunto no almacena datos duplicados
print(conjunto)

# Diccionarios:
diccionario = {
    # Clave/Key         : Valor
    "nombre"            : "pedro",
    "apellido"          : "perez",
    "dni"               : 12345234,
    "talle"             : 30            #Al final no se pone coma
}
print(diccionario["nombre"]) #imprime: pedro
print(diccionario["dni"])    #imprime el dni

