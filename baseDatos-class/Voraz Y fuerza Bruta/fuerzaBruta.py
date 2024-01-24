def buscar_subcadena(texto, subcadena):
    n = len(texto)
    m = len(subcadena)
    for i in range(n - m + 1):
        j = 0
        while j < m and texto[i + j] == subcadena[j]:
            j += 1
        if j == m:
            return i
    return -1

texto_completo = "Hola, ¿cómo estás?"
subcadena_buscar = "cómo"
resultado_fuerza_bruta = buscar_subcadena(texto_completo, subcadena_buscar)
if resultado_fuerza_bruta != -1:
    print(f"Subcadena encontrada en la posición {resultado_fuerza_bruta}")
else:
    print("Subcadena no encontrada.")