def combinar_listas(lista1, lista2):
    combinada = []
    for i in range(len(lista1)):
        combinada.append(lista1[i])
        combinada.append(lista2[i])
    return combinada

def pedir_lista(nombre_lista, cantidad):
    lista = []
    print(f"Vas a ingresar {cantidad} elementos para {nombre_lista}.")
    print("IMPORTANTE: escribe un solo dato por línea (sin comas)")
    for i in range(cantidad):
        elemento = input(f"{nombre_lista} - Elemento {i + 1}: ")
        lista.append(elemento)
    return lista


try:
    cantidad = int(input("¿Cuántos elementos quieres ingresar por lista?: "))
    if cantidad <= 0:
        print("Debe ser un número mayor que 0.")
        exit()
except ValueError:
    print("Por favor, ingresa un número entero válido.")
    exit()


lista1 = pedir_lista("Lista 1", cantidad)
lista2 = pedir_lista("Lista 2", cantidad)

lista_combinada = combinar_listas(lista1, lista2)

print("\nLista combinada:", lista_combinada)