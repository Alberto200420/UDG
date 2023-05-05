# Dado un arreglo de 100 elementos, implemente una solución - el pseudocodigo y diagrama de
# flujo que muestre un mensaje en pantalla si la suma de la primera mitad de los elementos del
# arreglo es igual, menor o mayor a la suma de la segunda mitad.

# Creamos el arreglo y lo inicializamos con números aleatorios
import random
arr = [random.randint(1, 10) for i in range(100)]

# Calculamos las sumas de las dos mitades del arreglo
suma_primera_mitad = sum(arr[:50])
suma_segunda_mitad = sum(arr[50:])

# Comparamos las sumas y mostramos un mensaje en pantalla
if suma_primera_mitad == suma_segunda_mitad:
    print("La suma de la primera mitad es igual a la suma de la segunda mitad")
elif suma_primera_mitad < suma_segunda_mitad:
    print("La suma de la primera mitad es menor que la suma de la segunda mitad")
else:
    print("La suma de la primera mitad es mayor que la suma de la segunda mitad")
