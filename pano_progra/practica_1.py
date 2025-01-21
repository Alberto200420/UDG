valores = []
valores_nulos = []


def limite():
  valor_a_revisar = float('inf')
  while valor_a_revisar != 0:
    valor_a_revisar = float(input("Ingresa el valor a revisar (0 para terminar): "))
    if valor_a_revisar == 0:
      break
          
    if valor_a_revisar >= limite_superior or valor_a_revisar <= limite_inferior:
      valores_nulos.append(valor_a_revisar)
    else:
      valores.append(valor_a_revisar)

  print(f"\nLos valores fuera de los limites: {valores_nulos}")
  print(f"Los valores dentro de los limites: {valores}")
  print(f"La suma de los valores dentro de los limites: {sum(valores)}")

limite_superior = float(input("Ingresa el limite superior: "))
limite_inferior = float(input("Ingresa el limite inferior: "))


if limite_inferior < limite_superior:
  limite()

print("error")