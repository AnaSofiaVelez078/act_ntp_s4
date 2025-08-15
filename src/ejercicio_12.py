# Función que solicita palabras al usuario hasta que escriba 'salir',
# almacena las palabras en un conjunto, y muestra cuántas únicas y cuáles se repitieron
def palabras_unicas_repetidas():
    palabras_unicas = set()   # Para almacenar palabras únicas
    palabras_vistas = {}      # Diccionario para contar apariciones

    print("Ingresa palabras (escribe 'salir' para terminar):")

    while True:
        palabra = input("> ").strip().lower()  # Normalizar palabra

        if palabra == 'salir':
            break

        # Contar ocurrencias usando diccionario
        if palabra in palabras_vistas:
            palabras_vistas[palabra] += 1
        else:
            palabras_vistas[palabra] = 1
            palabras_unicas.add(palabra)  # Solo se agrega si es la primera vez

    # Detectar palabras repetidas (apariciones > 1)
    repetidas = [p for p, count in palabras_vistas.items() if count > 1]

    # Mostrar resultados
    print(f"\nCantidad de palabras únicas ingresadas: {len(palabras_unicas)}")
    if repetidas:
        print("Palabras repetidas:", ', '.join(repetidas))
    else:
        print("No se ingresaron palabras repetidas.")

# Ejecutar la función
palabras_unicas_repetidas()
