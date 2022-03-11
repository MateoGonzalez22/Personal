n = int(input("Cantidad: "))
caracter = input("Caracter: ")


def generar(n, caracter):
    for x in range(0, n):
        print(caracter, end = "")

generar(n, caracter)