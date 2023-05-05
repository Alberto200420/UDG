# Hacer el pseudocodigo y diagrama de flujo que lea N valores, y los almacene en un arreglo.
# Una vez almacenados recorra una posición hacia arriba quedando el primero en el último, el
# segundo en el primero, el tercero en el segundo y así sucesivamente. El diagrama terminará
# cuando se lea un número igual a cero que no se procesará, y no se leerán más de 30 números.

# Creamos el arreglo y lo inicializamos con ceros
arr = [0] * 30

# Leemos los valores y los almacenamos en el arreglo
n = 0
while n < 30:
    valor = int(input("Ingrese un número (o 0 para terminar): "))
    if valor == 0:
        break
    arr[n] = valor
    n += 1

# Recorremos el arreglo una posición hacia arriba
ultimo_valor = arr[n-1]
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = ultimo_valor

# Mostramos el arreglo resultante
print("El arreglo resultante es:", arr[:n])