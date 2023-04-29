# Hacerl el pseudocodigo y diagrama de flujo que almacene 100 datos numericos en un arreglo, una vez almacenado se 
# busque el valor maximo y vlaor minimo y lo muestre en la pantalla junto con su posicion

# Definimos la lista para almacenar los números
numeros = []

# Pedimos al usuario que ingrese los 100 números y los almacenamos en la lista
for i in range(100):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

# Buscamos el valor máximo y mínimo y sus posiciones en la lista
maximo = numeros[0]
minimo = numeros[0]
pos_maximo = 0
pos_minimo = 0

for i in range(1, len(numeros)):
    if numeros[i] > maximo:
        maximo = numeros[i]
        pos_maximo = i
    elif numeros[i] < minimo:
        minimo = numeros[i]
        pos_minimo = i

# Imprimimos los resultados
print("El valor máximo es", maximo, "y está en la posición", pos_maximo)
print("El valor mínimo es", minimo, "y está en la posición", pos_minimo)
