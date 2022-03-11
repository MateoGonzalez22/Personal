palabra = input("Ingrese la palabra: ")

vocales = ["a", "e", "i", "o", "u"]

cantvocales = 0

for i in palabra:
    if i in vocales:
        cantvocales = cantvocales + 1

print(cantvocales)