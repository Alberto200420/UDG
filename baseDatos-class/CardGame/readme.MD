# Card game with python

## Descripción
I did this project in order to exempt in algorithms and databases class.
It's basically a Spanish card game against the computer, it's very basic, I didn't put much effort into it, it has bugs but it works.

feel free to use the code to learn, you can download it to play with it and if you want to contribute contributions are welcome! Please create a pull request.

## Analizis en Big O:

## 1- `repitedNumber()` en la clase Computer:

```python
  def repitedNumber(self, mano):
    id_counts = {}
    for carta in mano:
      current_id_count = id_counts.get(carta["id"], 0)
      id_counts[carta["id"]] = current_id_count + 1
    # Filtrar los ids que se repiten más de 3 veces
    repeated_ids = {id: count for id, count in id_counts.items() if count > 1}
    # id_counts.items(): Esto devuelve una vista de los elementos del diccionario id_counts en forma de tuplas (clave, valor).
    # for id, count in ...: Establece un bucle sobre esas tuplas, desempaquetando cada tupla en dos variables: id y count.
    # if count >= 3: Agrega una condición para incluir solo las tuplas donde el valor (count) sea mayor o igual a 3.
    # {id: count for ...}: Crea un nuevo diccionario utilizando la sintaxis de comprensión de diccionario. 
    # En este diccionario, las claves (id) son las claves del diccionario original (id_counts), y los valores son los valores 
    # correspondientes (count),pero solo para las tuplas que cumplen la condición count >= 3.
    # Entonces, en resumen, repeated_ids será un nuevo diccionario que contiene solo los elementos de id_counts 
    # donde el valor asociado (count) es mayor o igual a 1. Esto te da un diccionario filtrado con los ids que se repiten 
    # más de 1 veces y la cantidad de repeticiones.
    return repeated_ids
```
Recorre la lista de cartas (mano).
Utiliza un diccionario `id_counts` para contar la cantidad de repeticiones de cada `id`.
Filtra los `id` que se repiten más de una vez.
Devuelve un diccionario con los 'id' que se repiten.
La complejidad temporal de esta función sería O(n), donde 'n' es la longitud de la lista de cartas (mano). Esto se debe a que se recorre la lista una vez.


## 2- `retornadDibujo()` en la clase Computer:
```python
  def retornadDibujo(self, cartas):
    # Diccionario para almacenar los 'id' correspondientes a cada 'dibujo'
    diccionario_resultado = {}

    for carta in cartas:
      dibujo_actual = carta['dibujo']
      id_actual = carta['id']

      # Si el 'dibujo' no está en el diccionario, se agrega con una lista que contiene el 'id'
      if dibujo_actual not in diccionario_resultado:
        diccionario_resultado[dibujo_actual] = [id_actual]
      else:
        # Si el 'dibujo' ya está en el diccionario, se agrega el 'id' a la lista existente
        diccionario_resultado[dibujo_actual].append(id_actual)
    for dibujo, lista_id in diccionario_resultado.items():
      diccionario_resultado[dibujo] = sorted(lista_id)

    return diccionario_resultado
```
Recorre la lista de cartas.
Utiliza un diccionario `diccionario_resultado` para almacenar los `id` correspondientes a cada `dibujo`.
Devuelve un diccionario donde las claves son los `dibujos` y los valores son listas ordenadas de `id` asociados.
Al igual que repitedNumber, la complejidad temporal de esta función sería O(n), donde 'n' es la longitud de la lista de cartas.

## En general, el algoritmo principal de la clase `Computer` tiene una complejidad temporal de O(n), donde 'n' es la longitud de la lista de cartas (mazo). Esto se debe a que se recorre la lista una vez en el bucle principal del juego.

# ANALIZANDO `cardGame.py`

## Inicialización y Distribución de Cartas:
```python
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
```

La inicialización y distribución de las cartas tiene una complejidad O(1), ya que son operaciones de tiempo constante.


## Bucle Principal `for cartas in mazo[14:]`:

Este bucle recorre las cartas desde la posición 14 hasta el final.
Dentro del bucle, hay llamadas a funciones como comparationComputer y comparationUser, cada una de las cuales tiene complejidad O(n) para buscar y manipular listas.
La función pritnMazo imprime las cartas del usuario, lo cual también es O(n).

## Función `bajarCartas()`:

```python
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
```
Esta función solicita al usuario ingresar la cantidad de cartas que desea bajar y luego solicita las posiciones de las cartas a eliminar.
Las operaciones de agregar y eliminar elementos de la lista cartasUsuario son O(n) en el peor caso, ya que se realizan dentro de bucles.


## Complejidad General:

En general, la complejidad temporal del programa principal es dominada por el bucle principal y las operaciones dentro de las funciones llamadas en cada iteración.
Dado que las funciones llamadas (comparationComputer, comparationUser, y bajarCartas) tienen complejidad O(n), la complejidad total del programa principal es O(n^2), donde 'n' es el tamaño del mazo.


## En cuanto al tipo de algoritmo, este código parece ser una implementación de un juego de cartas interactivo entre un usuario y una computadora. No se ajusta a un tipo de algoritmo clásico y se centra en la lógica del juego y la interacción del usuario.

## En resumen, la complejidad temporal del código principal es O(n^2), y el tipo de algoritmo se puede describir como un juego de cartas interactivo.