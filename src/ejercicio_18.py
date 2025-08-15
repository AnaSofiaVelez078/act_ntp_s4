def agenda_telefonica():
    agenda = {}

    while True:
        print("\n--- Menú Agenda ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del contacto: ").strip()
            telefono = input("Número de teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")

        elif opcion == '2':
            nombre = input("Nombre a buscar: ").strip()
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print(f"Contacto '{nombre}' no encontrado.")

        elif opcion == '3':
            if agenda:
                print("\nContactos:")
                for nombre, telefono in agenda.items():
                    print(f"- {nombre}: {telefono}")
            else:
                print("La agenda está vacía.")

        elif opcion == '4':
            nombre = input("Nombre a eliminar: ").strip()
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print(f"Contacto '{nombre}' no encontrado.")

        elif opcion == '5':
            print("Saliendo de la agenda.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    agenda_telefonica()
