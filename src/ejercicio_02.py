def pedir_calificaciones():
    calificaciones = []

    while True:
        entrada = input("Ingresa una calificación (o escribe 'fin' para terminar): ")
        
        if entrada.lower() == 'fin':
            break
        
        if entrada.replace('.', '', 1).isdigit():
            calificaciones.append(float(entrada))
        else:
            print("⚠️ Entrada inválida. Por favor, ingresa un número o 'fin'.")

    if len(calificaciones) > 0:
        promedio = sum(calificaciones) / len(calificaciones)
        nota_mas_alta = max(calificaciones)
        nota_mas_baja = min(calificaciones)

        print("\n📊 Resultados:")
        print("Promedio:", round(promedio, 2))
        print("Nota más alta:", nota_mas_alta)
        print("Nota más baja:", nota_mas_baja)
    else:
        print("No ingresaste ninguna calificación.")

pedir_calificaciones()
