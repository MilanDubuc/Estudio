""" Ej.1 video del bobo
lista = [4, 6, 7, 4, 3, 2, 3, 4]
cuco = 4


def pepe (nums, val):
    k = 0
    while nums.contains(val):
        nums.remove(val)
        k += 1
    return k

print(pepe(lista, cuco))
print(lista)

print(dir(lista))
"""

"""ordena segun cant de vocales
def clave(x):
    vocales = ["a", "e", "i", "o", "u"]
    cont = 0
    for i in range(5):
        cont += x[0].count(vocales[i-1])
    return cont


lista = [("hola puto", 12), ("alohe", 22), ('zorro', 5)]

lista.sort(key=clave)
print(lista)
"""

