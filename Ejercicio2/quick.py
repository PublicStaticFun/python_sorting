def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    centro = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]
    return quick_sort(izquierda) + centro + quick_sort(derecha)

tiempos_entrega = [12, 4, 24, 6, 3, 15]
resultado = quick_sort(tiempos_entrega)
print("Tiempos ordenados: ", resultado)