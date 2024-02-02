def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio  # Elemento encontrado, devuelve el índice.
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Elemento no encontrado.

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = int(input("Elememto a buscar: "))

resultado = busqueda_binaria(mi_lista, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")

# Inicio: El diagrama comienza con el inicio del programa.

# Entrada de Datos: Se usa un rombo para representar la entrada de datos, 
# donde el usuario ingresa el elemento que desea buscar en la lista.

# Inicialización de Variables: Se asignan valores iniciales a las variables 
# izquierda y derecha (rombos de procesamiento).

# Bucle While: Se utiliza un rectángulo con una condición para representar el bucle while. 
# La condición es que izquierda sea menor o igual a derecha.

# Cálculo del Punto Medio: Se calcula el punto medio entre izquierda y derecha. 
# Esto se representa con un rombo de procesamiento.

# Comparación: Se utiliza un rombo de decisión para comparar el elemento en la posición media con el elemento buscado.

# Si son iguales, se ha encontrado el elemento y el programa termina.
# Si el elemento en la posición media es menor que el elemento buscado, 
# se actualiza izquierda para buscar en la mitad derecha.
# Si el elemento en la posición media es mayor que el elemento buscado, 
# se actualiza derecha para buscar en la mitad izquierda.
# Fin del Bucle While: Cuando la condición del bucle while no se cumple, 
# se sale del bucle y se llega a un rombo de proceso que representa el final del programa.

# Salida de Resultados: Se utiliza un rectángulo para mostrar si se encontró o no el elemento, y en qué posición.

# Fin: El diagrama concluye con el fin del programa.