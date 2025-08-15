# Función que genera dos conjuntos y muestra operaciones entre ellos
def conjuntos_pares_multiplos():
    # Crear conjunto de números pares del 2 al 20 usando ciclo for
    pares = set()
    for num in range(2, 21):
        if num % 2 == 0:
            pares.add(num)

    # Crear conjunto de múltiplos de 3 del 3 al 30 usando ciclo for
    multiplos_3 = set()
    for num in range(3, 31):
        if num % 3 == 0:
            multiplos_3.add(num)

    # Mostrar los conjuntos
    print("Conjunto de pares (2-20):", pares)
    print("Conjunto de múltiplos de 3 (3-30):", multiplos_3)

    # Operaciones entre conjuntos
    union = pares.union(multiplos_3)
    interseccion = pares.intersection(multiplos_3)
    diferencia = pares.difference(multiplos_3)
    diferencia_simetrica = pares.symmetric_difference(multiplos_3)

    # Mostrar resultados de operaciones
    print("\nUnión:", union)
    print("Intersección:", interseccion)
    print("Diferencia (pares - múltiplos de 3):", diferencia)
    print("Diferencia simétrica:", diferencia_simetrica)

# Ejecutar la función
conjuntos_pares_multiplos()
