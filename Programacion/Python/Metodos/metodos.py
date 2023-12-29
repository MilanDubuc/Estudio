#metodos:
# Dato.metodo()
texto = "la pUTa mAdre"
print(dir(texto)) #dir() devuelve una lista de atributos validos, osea, acciones validas.
print("texto: " + texto)
#mas comunes:
#upper
print("upper: %s" %(texto.upper()))
#lower
print("lower: %s" %(texto.lower()))
#capitalize - primeras letras mayus
print("capitalize: %s" %(texto.capitalize()))
#find - encuentra la primera aparicion de a en b, sino devuelve 1
print("find(a): %s" %(texto.find("a")))
print("find(z): %s" %(texto.find("z")))
#index - encuentra la primera aparicion de a en b, sino devuelve una excepcion
print("index(a): %s" %(texto.index("a")))
print("index(z): tira error/excepcion")
#isnumeric
print("isnumeric: %s" %(texto.isnumeric()))
#isalpha - es alphanumerico (el espacio NO es apfanumerico)
print("isalpha: %s" %(texto.isalpha()))
#count - devuelve el numero de ocurrencias de a en b
print("count(a): %s" %(texto.count("a")))
#len - (length) cuenta los caracteres de. es una funcion
print("len(texto): %s" %(len(texto)))
#endswith - verifica si b termina con a 
print("endswith(dre): %s" %(texto.endswith("dre")))
print("endswith(la): %s" %(texto.endswith("la")))
#startswith - verifica si b termina con a 
print("startswith(dre): %s" %(texto.startswith("dre")))
print("startswith(la): %s" %(texto.startswith("la")))
#replace -  reepmplaza a dentro de b con c
print("replace(la, el): %s" %(texto.replace("la", "el")))
#split - separa b cada vez que encuantra a
print("split(' '): %s" %(texto.split(" ")))