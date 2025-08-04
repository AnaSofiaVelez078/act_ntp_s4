def carrito_compras():
    carrito = []

    while True:
        print("\n--- MENÚ CARRITO DE COMPRAS ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                producto = {"nombre": nombre, "precio": precio}
                carrito.append(producto)
                print(f"{nombre} fue agregado al carrito.")
            except ValueError:
                print("Precio inválido. Intenta de nuevo.")
        
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            encontrado = False
            for producto in carrito:
                if producto["nombre"].lower() == nombre.lower():
                    carrito.remove(producto)
                    print(f"{nombre} fue eliminado del carrito.")
                    encontrado = True
                    break
            if encontrado:
                print("Producto no encontrado.")
        
        elif opcion == "3":
            if carrito:
                print("El carrito está vacío.")
            else:
                print("\nProductos en el carrito:")
                for i, producto in enumerate(carrito, start=1):
                    print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
        
        elif opcion == "4":
            total = sum(producto["precio"] for producto in carrito)
            print(f"Total a pagar: ${total:.2f}")
        
        elif opcion == "5":
            print("Gracias por usar el carrito de compras.")
            break
        
        else:
            print("Opción inválida. Intenta otra vez.")
            
carrito_compras () 