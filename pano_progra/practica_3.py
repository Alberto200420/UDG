dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
datos = {}

def obtener_valores(nombre):
  valores = {}
  print(f"\nIngrese los valores para {nombre}:")
  for dia in dias:
    try:
      valor = float(input(f"{dia}: "))
      valores[dia] = valor
    except ValueError:
      print("Por favor, ingrese un número válido")
  return valores

def encontrar_maximo(datos):
  max_valor = float('-inf')
  max_nombre = ""
  max_dia = ""
    
  for nombre, valores in datos.items():
    for dia, valor in valores.items():
      if valor > max_valor:
        max_valor = valor
        max_nombre = nombre
        max_dia = dia
    
  return max_nombre, max_dia, max_valor


for i in range(5):
  nombre = input(f"\nIngrese el nombre de la persona {i+1}: ")
  datos[nombre] = obtener_valores(nombre)

nombre_max, dia_max, valor_max = encontrar_maximo(datos)

print("\n=== Resultado ===")
print(f"El valor más alto es: {valor_max}")
print(f"Corresponde a: {nombre_max}")
print(f"En el día: {dia_max}")