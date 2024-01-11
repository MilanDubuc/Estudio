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

#si el modulo esta en una carpeta mas arriba que el archivo:
#python busca en sys.path cada vez que importo algo. Si lo que quiero importar no esta en sys.path simplemente lo tengo que agregar:
"""
import sys
sys.path.append("Aca va el directorio de lo que queremos importar(c\usuario\etc)")
"""

#Paquetes:
"""
-un paquete es una carpeta con varios modulos
-la carpeta paquete tiene que tener un archivo llamado __init__.py para que python lo interprete como paquete
-luego para importar:
import paquete.modulo_func_paquete
"""

