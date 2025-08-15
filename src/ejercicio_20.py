def sistema_temperaturas():
    # Diccionario: ciudad -> {día: temperatura}
    datos = {}

    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    while True:
        print("\n--- Menú Sistema de Temperaturas ---")
        print("1. Agregar ciudad")
        print("2. Registrar temperatura")
        print("3. Mostrar temperaturas de una ciudad")
        print("4. Estadísticas por ciudad")
        print("5. Estadísticas por día")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            ciudad = input("Nombre de la ciudad: ").strip()
            if ciudad not in datos:
                datos[ciudad] = {dia: None for dia in dias_semana}
                print(f"Ciudad '{ciudad}' agregada.")
            else:
                print("Ciudad ya existe.")

        elif opcion == '2':
            ciudad = input("Ciudad: ").strip()
            if ciudad in datos:
                print("Días disponibles:", ', '.join(dias_semana))
                dia = input("Día de la semana: ").strip()
                if dia in dias_semana:
                    try:
                        temp = float(input("Temperatura registrada: "))
                        datos[ciudad][dia] = temp
                        print(f"Temperatura para {ciudad} el {dia} registrada.")
                    except ValueError:
                        print("Temperatura inválida.")
                else:
                    print("Día inválido.")
            else:
                print("Ciudad no encontrada.")

        elif opcion == '3':
            ciudad = input("Ciudad a mostrar: ").strip()
            if ciudad in datos:
                print(f"Temperaturas de {ciudad}:")
                for dia, temp in datos[ciudad].items():
                    print(f"  {dia}: {temp if temp is not None else 'No registrada'}")
            else:
                print("Ciudad no encontrada.")

        elif opcion == '4':
            ciudad = input("Ciudad para estadísticas: ").strip()
            if ciudad in datos:
                temps = [t for t in datos[ciudad].values() if t is not None]
                if temps:
                    promedio = sum(temps) / len(temps)
                    minimo = min(temps)
                    maximo = max(temps)
                    print(f"Estadísticas para {ciudad}:")
                    print(f"  Promedio: {promedio:.2f}")
                    print(f"  Mínima: {minimo}")
                    print(f"  Máxima: {maximo}")
                else:
                    print("No hay temperaturas registradas para esta ciudad.")
            else:
                print("Ciudad no encontrada.")

        elif opcion == '5':
            dia = input("Día para estadísticas: ").strip()
            if dia in dias_semana:
                temps_dia = [datos[ciudad][dia] for ciudad in datos if datos[ciudad][dia] is not None]
                if temps_dia:
                    promedio = sum(temps_dia) / len(temps_dia)
                    minimo = min(temps_dia)
                    maximo = max(temps_dia)
                    print(f"Estadísticas para el día {dia}:")
                    print(f"  Promedio: {promedio:.2f}")
                    print(f"  Mínima: {minimo}")
                    print(f"  Máxima: {maximo}")
                else:
                    print("No hay temperaturas registradas para este día.")
            else:
                print("Día inválido.")

        elif opcion == '6':
            print("Saliendo del sistema de temperaturas.")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    sistema_temperaturas()
