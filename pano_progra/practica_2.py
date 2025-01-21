mes = 1
dinero = []
while mes <= 12:
  ahorro = float(input(f"Ingresa el dinero que ahorraras en el mes {mes}: "))
  if ahorro <= 0:
    print("Invalido")
    continue
  dinero.append(ahorro)
  mes += 1

print(f"Esto es el total que obtendras al final del año: {sum(dinero)}")