import random

def rellenar_array_tamano_n(n):
    array = [random.randint(1, 100) for _ in range(n)]
    return array

# Ejemplo de uso
tamanio_array = int(input("De que tamaño quieres que sea el array? "))
mi_array = rellenar_array_tamano_n(tamanio_array)
print("Array generado:", mi_array)
