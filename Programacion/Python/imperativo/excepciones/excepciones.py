#con try intenta ejecutar el codigo, si tira una excepcion, aborta y ejecuta lo de except
def sumar():
    while True:
        a = int(input("Ingrese numero 1: "))
        b = int(input("Ingrese numero 2: "))
        try:
            resultado = a + b
            break
        except:
            print("Error, Ingrese un numero")
    return resultado