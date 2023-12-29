B = [10, 20, 45, 13]


for A in B:     #itera B y lo pone en A en cada bucle (B[0], B[1], etc)
    print(A)
    

#se pueden hacer dos for juntos:

animales = ["perro", "gato", "cocodrilo"]
es_mamifero = [True, True, False]

for animal,mamifero in zip(animales,es_mamifero):
    if mamifero:
        print("El %s es mamifero\n" %(animal))
    else:
        print("El %s no es mamifero\n" %(animal))
        
        
#iterar enteros: range():

for num in range(1,10):
    print(num)
    
#itera y enumera una lista: for a in enumerate(lista):
for i in enumerate(animales):
    print(i)

#Luego a[0] es el indice y a[1] es el valor
for j in enumerate(animales):
    print("el indice %d es el %s" %(j[0], j[1]))
    

#for, else: se ejecuta al terminar el for:

for num in range(5):
    print("Hola")
else:
    print("bueno, chau")
    

#el for funciona con listas, tuplas y conjuntos


#en diccionarios itera solo el key:
diccionario = {
    # clave = Dato
    ("nombre", "apellido"):['pedro', 'perez'], #tupla
    "dni":12345234, 
    "talle":30
}

for dic in diccionario:
    print(dic)
    
#para iterar los valore:

for dic in diccionario.values():
    print(dic)
    
#si queremos iterar todo, hay que poner:

for dic in diccionario.items(): 
    print(dic)                                      #dic[0] es el key y dic[1] es el dato
    print("el key es %s y el dato: %s" %(dic[0], dic[1]))
    

#con continue pasas al sigte ciclo
for num in range(10):
    if num == 5:
        continue
    print(num)
else:
    print("listo")
    
#con break salis del bucle, no ejecuta nada mas (ni siquiera el else)
for num in range(10):
    if num == 5:
        break
    print(num)
else:
    print("listo")
    
#tambien se puede:
# [accion for]:
[print(x) for x in range(5)]
    
    
    
    