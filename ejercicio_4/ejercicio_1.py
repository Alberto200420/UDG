# Hacer el pseudogcodigo que calcule la suma de los terminos de la serie de FIBONACCI coyos valores se encuentran 
# entre 100 y 10,000

# Definimos las variables para el cálculo
n1 = 0
n2 = 1
suma = 0

# Calculamos los términos de la serie de Fibonacci
while n2 < 10000:
    # Si el término actual está entre 100 y 10000, lo sumamos
    if n2 >= 100:
        suma += n2
    
    # Calculamos el siguiente término de la serie de Fibonacci
    temp = n2
    n2 += n1
    n1 = temp

# Imprimimos el resultado
print("La suma de los términos de la serie de Fibonacci entre 100 y 10,000 es:", suma)
