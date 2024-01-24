def cambio_voraz(monedas, cantidad):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            cambio.append(moneda)
    return cambio

monedas_disponibles = [25, 10, 5, 1]
cantidad_a_cambiar = int(input("Cantidad a cambiar: "))
resultado_voraz = cambio_voraz(monedas_disponibles, cantidad_a_cambiar)
print(f"Cambio voraz para {cantidad_a_cambiar} es: {resultado_voraz}")
