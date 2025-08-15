def contador_palabras(frase):
    frase = frase.lower()  # Ignorar mayúsculas
    palabras = frase.split()  # Dividir en palabras
    contador = {}

    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1

    # Ordenar por frecuencia descendente
    palabras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("Palabras ordenadas por frecuencia:")
    for palabra, freq in palabras_ordenadas:
        print(f"{palabra}: {freq}")


if __name__ == "__main__":
    texto = input("Ingresa una frase: ")
    contador_palabras(texto)
