lista = ['caca' , 12.5 , True , 1]
#len
print('len(lista): %s' %(len(lista)))

#append: agrega al final:
lista.append("pedro")
print('lista.append("pedro"),\nluego la lista queda: %s \n' %(lista))

#insert: agrega donde quieras
lista.insert(2, 'jiji')
print('lista.insert(2, "jiji"), \nluego la lista queda: %s \n' %(lista))

#extend: agrega al final otra lista
lista.extend([1, 2, 3, 4])
print("lista.extend(1, 2, 3, 4). \nla lista queda: %s \n" %(lista))

#pop: borra el indice especiicado
lista.pop(7)
print("lista.pop(7). \nla lista queda: %s \n" %(lista))

#remove: borra un elemento especiico
lista.remove('jiji')
print("lista.remove('jiji'). \nQueda: %s \n" %(lista))

#sort() de menor a mayor. sort(reverse): de mayor a menor
lista_num = [34, 12, 6, 98, 5, True, 23, False, 159]
print("Sort no funciona con strings.")
print("tenemos la lista: %s" %(lista_num))
lista_num.sort()
print("Luego de lista_num.sort(). \nQueda la lista: %s\n" %(lista_num))

#reverse: invierte la lista
lista_num.reverse()
print("lista_num.reverse(). \nLa lista queda: %s \n" %(lista_num))

#clear: borra todo
lista.clear()
print("lista.clear(). \nQueda: %s" %(lista))