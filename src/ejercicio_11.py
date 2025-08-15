# Función que recibe dos listas, las convierte en conjuntos usando ciclos for,
# y calcula las operaciones de unión, intersección, diferencia y diferencia simétrica
def operaciones_conjuntos(lista1, lista2):
    # Convertir lista1 a conjunto usando ciclo for
    conjunto1 = set()
    for elem in lista1:
        conjunto1.add(elem)

    # Convertir lista2 a conjunto usando ciclo for
    conjunto2 = set()
    for elem in lista2:
        conjunto2.add(elem)

    # Calcular unión
    union = conjunto1.union(conjunto2)

    # Calcular intersección
    interseccion = conjunto1.intersection(conjunto2)

    # Calcular diferencia (elementos en conjunto1 que no están en conjunto2)
    diferencia = conjunto1.difference(conjunto2)

    # Calcular diferencia simétrica (elementos que están en uno u otro pero no en ambos)
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

    # Mostrar resultados
    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia (conjunto1 - conjunto2):", diferencia)
    print("Diferencia simétrica:", diferencia_simetrica)

# Ejemplo de listas
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

# Llamar a la función
operaciones_conjuntos(lista_a, lista_b)
