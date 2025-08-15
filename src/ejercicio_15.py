# Función que recibe una lista y crea un conjunto con números únicos usando ciclo for
# Luego muestra cuántos duplicados había en la lista original
def contar_duplicados(lista):
    conjunto_unicos = set()  # Conjunto para almacenar números únicos

    # Agregar elementos a conjunto usando ciclo for
    for num in lista:
        conjunto_unicos.add(num)

    # Calcular cantidad de duplicados
    total_original = len(lista)
    total_unicos = len(conjunto_unicos)
    duplicados = total_original - total_unicos

    # Mostrar resultados
    print(f"Tamaño original de la lista: {total_original}")
    print(f"Números únicos en el conjunto: {total_unicos}")
    print(f"Cantidad de duplicados: {duplicados}")

# Ejemplo de uso
lista_numeros = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]
contar_duplicados(lista_numeros)
