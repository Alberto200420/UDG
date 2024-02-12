import json
from random import shuffle
from computerAlgoridm import Computer
computadora = Computer()

cartasComputadora = []
cartasUsuario = []
tableUser = []
tableComputer = []
turno = 0
maxId = {} # {12: 2, 10: 2}
dibujoRepited = {} # {'basto': [7, 12], 'espada': [11, 10], 'copa': [3], 'moneda': [10, 12]}

def pritnMazo():
  print('Tus cartas:')
  position = 1
  for carta in cartasUsuario:
    print(f'posicion {position}: {carta["dibujo"], carta["id"]}')
    position +=1

# ESTA FUNCIO BAJA CARTAS Y LAS ASIGNA A tableUser Y ELIMINA ESAS
# CARTAS DE LA MANO "cartasUsuario"
def bajarCartas():
  while True:
    pritnMazo()
    noCard = int(input(f'Cuantas cartas quieres bajar?: '))
    if noCard >= 3:
      break
    else:
      print("Por favor, ingresa al menos 3 cartas.")
  positionList = []
  for number in range(noCard):
    positions = int(input(f'Carta numero {number + 1} a eliminar, asigna la posicion de esa carta: '))
    tableUser.append(cartasUsuario[positions - 1])
    positionList.append(positions - 1)
  positionList.sort()
  for index in sorted(positionList, reverse=True):
    cartasUsuario.pop(index)

def comparationComputer(carta):
  global maxId
  if carta["id"] in maxId:
    cartasComputadora.append(carta)
    searchNo = carta["id"]
    posiciones = [i for i, carta in enumerate(cartasComputadora) if carta['id'] == searchNo]
    for position in posiciones:
      tableComputer.append(cartasComputadora[position])
    posiciones.sort()
    for index in sorted(posiciones, reverse=True):
      cartasComputadora.pop(index)
    # maxId = computadora.repitedNumber(cartasComputadora)
    print("A la computadora le sirbio la carta y bajo sus cartas")
    return 
  # elif carta["dibujo"] in dibujoRepited:
  #   # newList = computadora.agregarDibujo(carta, dibujoRepited)
  #   print(dibujoRepited)
  #   print(cartasComputadora)
  #   print("newList")
  #   return
  elif turno == 1:
    print("No le sirvio la carta a la computadora, la revisarás tu\n")
    comparationUser(carta)
    return
  print("No le sirvio la carta a la computadora\n")

def comparationUser(carta):
  global turno
  print(f'\nCarta obtenida: {cartas["dibujo"], cartas["id"]}')
  pritnMazo()
  option = str(input("\nTe sirve esta carta? yes/no: "))
  if option.lower() == "yes" or option.lower() == "y":
    cartasUsuario.append(carta)
    bajarCartas()
    print("Bajaste cartas a la mesa\n")
    return
  elif turno == 0 and option.lower() != "yes" or option.lower() == "y":
    print("No te sirvio la carta, la revisará la computadora")
    comparationComputer(carta)
    return
  print("No te sirvio la carta")
  
def asignacion():
  # ASIGNAR A CADA JUGADOR SUS CARTAS
  for carta in mazo[:7]:
    cartasComputadora.append(carta)
  for carta in mazo[7:14]:
    cartasUsuario.append(carta)

# ABRIR EL ARCIVO JSON
with open("card.json") as mazo:
  cartas = json.load(mazo)
# OBTENER EL MAZO
mazo = cartas["mazo"]
# MEZCLAR EL MAZO                       1
shuffle(mazo)
# REPARTE                               2
asignacion()
# FUNCION QUE RETORNA UN DICCIONARIO CON TODOS LOS ID QUE SE REPITEN COMO MINIMO 2 VECES
resultId = computadora.repitedNumber(cartasComputadora)
# FUNCION QUE RETORNA UN DICCIONARIO CON TODOS LOS DIBUJOS QUE SE REPITEN Y GUARDA SUS ID´S DE MENOR A MAYOR
resutlDubujo = computadora.retornadDibujo(cartasComputadora)

for cartas in mazo[14:]:
  if turno == 0:
    print(f'Las cartas en la mesa de la computadora: {tableComputer}')
    turno = 1
    print(f'Computadora sacó: {cartas["dibujo"], cartas["id"]}')
    if resultId and resutlDubujo:
      maxId = resultId
      dibujoRepited = resutlDubujo
    comparationComputer(cartas)
  else:
    turno = 0
    print(f'Tus cartas en la mesa: {tableUser}')
    comparationUser(cartas)