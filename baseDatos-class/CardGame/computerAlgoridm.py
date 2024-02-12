class Computer:

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
  
  # def agregarDibujo(self, cartas, newCard):
  #   # witelsit = [
  #   #   {id: [1,2,3]},
  #   #   {id: [2,3,4]},
  #   #   {id: [3,4,5]},
  #   #   {id: [4,5,6]},
  #   #   {id: [5,6,7]},
  #   #   {id: [6,7,10]},
  #   #   {id: [7,10,11]},
  #   #   {id: [10,11,12]}
  #   # ]
  #   dibujo = newCard['dibujo']
  #   id_nuevo = newCard['id']
  #   cartas[dibujo].append(id_nuevo)
  #   for dibujo, lista_id in cartas.items():
  #     cartas[dibujo] = sorted(lista_id)
    
  #   return cartas
    