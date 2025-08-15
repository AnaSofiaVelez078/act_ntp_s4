def gestion_calificaciones():
    estudiantes = {}  # nombre: lista de calificaciones

    def agregar_estudiante(nombre):
        if nombre not in estudiantes:
            estudiantes[nombre] = []
            print(f"Estudiante '{nombre}' agregado.")
        else:
            print(f"El estudiante '{nombre}' ya existe.")

    def agregar_calificacion(nombre, calificacion):
        if nombre in estudiantes:
            estudiantes[nombre].append(calificacion)
            print(f"Calificación {calificacion} agregada a '{nombre}'.")
        else:
            print(f"Estudiante '{nombre}' no encontrado.")

    def calcular_promedio(nombre):
        if nombre in estudiantes and estudiantes[nombre]:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"Promedio de '{nombre}': {promedio:.2f}")
        else:
            print(f"No hay calificaciones para '{nombre}'.")

    while True:
        print("\n--- Menú Gestión de Calificaciones ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del estudiante: ").strip()
            agregar_estudiante(nombre)

        elif opcion == '2':
            nombre = input("Nombre del estudiante: ").strip()
            try:
                calificacion = float(input("Calificación a agregar: "))
                agregar_calificacion(nombre, calificacion)
            except ValueError:
                print("Calificación inválida.")

        elif opcion == '3':
            nombre = input("Nombre del estudiante: ").strip()
            calcular_promedio(nombre)

        elif opcion == '4':
            if estudiantes:
                print("\nEstudiantes y sus calificaciones:")
                for nom, notas in estudiantes.items():
                    print(f"- {nom}: {notas}")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == '5':
            print("Saliendo de gestión de calificaciones.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    gestion_calificaciones()
