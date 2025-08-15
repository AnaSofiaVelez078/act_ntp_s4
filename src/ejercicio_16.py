def inventario():
    inventario = {}  # Diccionario producto:cantidad

    while True:
        print("\n--- Menú Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            producto = input("Nombre del producto: ").strip()
            cantidad = int(input("Cantidad a agregar: "))
            if producto in inventario:
                print(f"Producto '{producto}' ya existe. Usa actualizar para modificar.")
            else:
                inventario[producto] = cantidad
                print(f"Producto '{producto}' agregado con cantidad {cantidad}.")

        elif opcion == '2':
            producto = input("Producto a actualizar: ").strip()
            if producto in inventario:
                cantidad = int(input("Nueva cantidad: "))
                inventario[producto] = cantidad
                print(f"Cantidad del producto '{producto}' actualizada a {cantidad}.")
            else:
                print(f"Producto '{producto}' no encontrado.")

        elif opcion == '3':
            producto = input("Producto a eliminar: ").strip()
            if producto in inventario:
                del inventario[producto]
                print(f"Producto '{producto}' eliminado.")
            else:
                print(f"Producto '{producto}' no encontrado.")

        elif opcion == '4':
            if inventario:
                print("\nInventario actual:")
                for prod, cant in inventario.items():
                    print(f"- {prod}: {cant}")
            else:
                print("Inventario vacío.")

        elif opcion == '5':
            print("Saliendo del inventario.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    inventario()
