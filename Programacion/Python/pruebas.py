
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