#con import agregamos las funciones en modulo_unciones
import modulo_funciones

#para usar una uncion de un modulo se pone: nombreModulo.funcion(parametro)
#ej;
print(modulo_funciones.saludo("pedro"))

#se puede importar con otro nombere:
"""se puede:

import modulo_funciones as f

luego seria:

print(f.saludo("pedro"))
"""

#se puede tambien importar SOLO UNA funcion perteneciente al modulo:
"""
seria:

from modulo_funciones import saludo

luego no hay que poner modulo.funciones.saludo, solo:

saludo("pedro")
(es como si la funcion estuviera definida en el mismo archivo, no hay que hacer referencia al modulo)
"""
#pedo