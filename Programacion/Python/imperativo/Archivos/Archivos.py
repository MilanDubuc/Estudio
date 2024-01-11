#para abrir un archivo:
archivo = open("Programacion\\Python\\imperativo\\Archivos\\archivo_texto.txt",encoding="UTF-8") #usa la ruta de acceso relativa. El encoding es para que reconozca mas caracteres
#archivo = open("archivo_texto.txt") se supone que si el archivo esta en la misma carpeta lo encuentra y funciona tambien

print(archivo)
#imprime cualquiera, hay que hacer:

print(archivo.read())
#deja el cursor al final

archivo.seek(0) #mueve el curso al princiopio, es necesario para volver a leerlo

#con readlines() me devuelve una lista de las lineas
print(archivo.readlines())

archivo.close() #cierra el archivo

#con with open("directorio") as Nombre, abre, ejecuta y cierra el archivo. Es como una funcion que usa el archivo

with open("Programacion\\Python\\imperativo\\Archivos\\archivo_texto.txt") as archivo:
    lineas = archivo.readlines()
    print(lineas[0])
#aca ya cerro el archivo

#modos de apertura:
"""
Access modes govern the type of operations possible in the opened file.

Read Only (r) : el cursor abre al principio
Read and Write (r+) : ""
Append and Read (a+) : el cursor abre al final
"""
#con archivo.write() sobreescrive el archivo

# con writelines te permite pasarle una lista; escribe los elementos uno despues de otro
lista = ["perro\n", "gato\n", "perdicion\n"]
with open("Programacion\\Python\\imperativo\\Archivos\\archivo_texto.txt", "r+") as archivo:
    print(archivo.readlines()) #deja el cursor al final
    archivo.writelines(lista)  #escrive a partir del cursor
    archivo.seek(0)            
    print(archivo.read())
    archivo.seek(0)
    print(archivo.readlines())


with open("Programacion\\Python\\imperativo\\Archivos\\archivo_texto.txt", "a+") as archivo:
    print("\nAhora:" + archivo.read()) # no lee por que abre con el cursor al final (a+)











