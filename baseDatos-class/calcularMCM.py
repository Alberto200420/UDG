def arrayDeCien(num):
    array = []
    i = 1
    while i <= 100:
        array.append(num * i)
        i = i + 1
    return array

def calcular_mcm_tabla(nums):
    # Este código es útil cuando necesitas encontrar el valor máximo en 
    maximo = max(nums) # una colección de datos y deseas almacenarlo en una variable para su posterior uso.
    listaMaximo = arrayDeCien(maximo)

    minimo = min(nums) # Encuentra el minimo

    i = 1

    while minimo != 0:
        resultado = minimo * i
        i = i + 1
        if resultado in listaMaximo:
            return resultado
            
numeros = []
numeroUno = int(input('ingresa el primer numero: '))
numeroDos = int(input('ingresa el segundo numero: '))
numeros.append(numeroUno)
numeros.append(numeroDos)
resultado = calcular_mcm_tabla(numeros)
print(f"El MCM de {numeros} es {resultado}")