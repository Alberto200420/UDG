# Hacer el pseudocodigo que almacene 20 numeros en un arreglo, una vez almacenados que genre un arreglo con los 
# numeros pares y otro arreglo con los impares, finalmente imprimir una columna con pares y la otra con los impares.

# Definimos la lista para almacenar los números
numeros = []

# Pedimos al usuario que ingrese los 20 números y los almacenamos en la lista
for i in range(20):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

# Definimos las listas para almacenar los números pares e impares
pares = []
impares = []

# Separamos los números pares e impares en sus respectivas listas
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprimimos los resultados
print("{:<10}{}".format("Pares", "Impares"))
for i in range(max(len(pares), len(impares))):
    if i < len(pares):
        print("{:<10}".format(pares[i]), end="")
    else:
        print("{:<10}".format(""), end="")
    if i < len(impares):
        print(impares[i])
    else:
        print("")
