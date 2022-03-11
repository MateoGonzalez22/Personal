arr = ["mañana", "hola", "chau", "vida", "computadora"]
arr2 = []
cant = 5

def filtrar(arr, cant):

    for i in arr:
        if len(i) >= cant:
            arr2.append(i)

filtrar(arr, cant)

print(arr2)