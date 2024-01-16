#un metodo es una funcion dentro de una clase
"""
el metodo sirve para crear una funcion que use los atributos especificos del objeto
para se le pasa como parametro "self":
"""
class Auto:
    def __init__(self, init_marca, init_modelo, init_precio): #con self se llama a si misma la funcion (self.marca es lo miusmo que Auto.marca)
        self.marca = init_marca      #crea el atributo y lo inicializa con valor igual al parametro pasado (init_blabla).
        self.modelo = init_modelo
        self.precio = init_precio
        
    def vender(self):
        print("se vendio el %s %s por %dUSD" %(self.marca, self.modelo, self.precio))


auto1 = Auto("golcito", "98", 3000)
auto2 = Auto("toyota", "supra", 100000)

auto1.vender()