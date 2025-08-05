def pedir_lista_palabras():
    lista = []
    cantidad = int(input("¿Cuántas palabras quieres ingresar a la lista? "))
    
    for i in range(cantidad):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista.append(palabra)
    
    return lista

def buscar_palabras_con_letra(palabras):
    letra_buscada = input("Ingresa una letra para buscar en las palabras: ").lower()
    palabras_encontradas = []

    for palabra in palabras:
        for letra in palabra:
            if letra.lower() == letra_buscada:
                palabras_encontradas.append(palabra)
                break

    return palabras_encontradas


lista_palabras = pedir_lista_palabras()

resultado = buscar_palabras_con_letra(lista_palabras)

print("Palabras que contienen la letra que ingresaste:", resultado)