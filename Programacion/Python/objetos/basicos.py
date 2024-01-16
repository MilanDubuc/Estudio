"""
POO:

clases: como la receta (el tipo de objeto; cualidades, etc)

class NombreClase():
    propiedad1 = "Valor"
    propiedad2 = "Valor"
    propiedad3 = "Valor"

ej;
"""
class Celular():
    marca = "Valor"     #propiedad1/atributo1
    modelo = "Valor"    #propiedad2/atributo2
    camara = "Valor"    #propiedad3/atributo3

"""
objeto: es una instancia de una clase
ej;
"""
celular1 = Celular()    #un objeto "celular"
celular2 = Celular()    #otro objeto celular

#de esta forma cuando creo el objetose "inicializa" sin los atributos definidos
#por eso se crea una funcion __init__ que se ejecuta siempre que uno crea el objeto (instancia la clase), donde podemos inicializarlo con parametros distintos en cada objeto de la clase
# ej;

class Auto:
    def __init__(self, init_marca, init_modelo, init_precio): #con self se llama a si misma la funcion (self.marca es lo miusmo que Auto.marca)
        self.marca = init_marca      #crea el atributo y lo inicializa con valor igual al parametro pasado (init_blabla).
        self.modelo = init_modelo
        self.precio = init_precio
        
#luego para definir un objeto:

auto1 = Auto("Golcito", "98", 3000) #creo una instancia de Auto inicializada con los atributos que quiero
        

