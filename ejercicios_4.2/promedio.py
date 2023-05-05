# Hacer un diagrama de flujo y pseudo código que almacene 100 valores en un arreglo y muestre en
# pantalla el promedio.

# Importamos la librería para generar números aleatorios
import random

# Creamos el arreglo y lo inicializamos con 100 valores aleatorios entre 0 y 100
arr = [random.randint(0, 100) for i in range(100)]

# Calculamos la suma de los valores del arreglo
suma = sum(arr)

# Calculamos el promedio
promedio = suma / 100

# Mostramos el promedio en pantalla
print("El promedio de los valores del arreglo es:", promedio)
