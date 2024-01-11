diccionario = {
    "nombre" : 'pedro',
    "apellido" : 'perez',
    "dni" : 12323537
}

#keys: nos devuelve las keys
print("diccionario.keys: %s \n" %(diccionario.keys()))

#get("key"): devuelve el valor !! si no lo encuentra NO tira error como con "diccionario(key)"
print("diccionario.get(dni): %s \n" %(diccionario.get("dni")))
print("diccionario.get(asasgsdgh): %s \n" %(diccionario.get("asasgsdgh")))

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")
print("diccionario.pop('apellido'): \nQueda: \ndiccionario.items: %s" %(diccionario.items()))

