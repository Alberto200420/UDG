# Hacer un diagrama de flujo y pseudo código que almacene 20 valores en un arreglo “a” y 20
# valores en un arreglo “b”, una vez almacenados que se almacene en la posición 0 de un arreglo “c”
# la suma del primer elemento de “a” con el ultimo de “b”, en la posición 1 del arreglo “c” el
# segundo de “a” con el penúltimo de “b” y así sucesivamente.


# Creamos los arreglos a y b
a = []
b = []

for A in range(20):
    valor = int(input("Ingresa los valores del arreglo A: "))
    a.append(valor)

for B in range(20):
    valor = int(input("Ingresa los valores del arreglo B: "))
    b.append(valor)



# Creamos el arreglo c
c = []

# Iteramos desde 0 hasta 9
for i in range(20):
    # Obtenemos el índice correspondiente en el arreglo b
    j = 19 - i
    
    # Sumamos el elemento correspondiente de a y b y lo almacenamos en res
    res = a[i] + b[j]

    c.append(res)

# Imprimimos los arreglos para verificar que todo haya funcionado correctamente
print("Arreglo a:", a)
print("Arreglo b:", b)
print("Arreglo c:", c)