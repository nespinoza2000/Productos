# Lista global de productos
productos = []


# Función para añadir un producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")

    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número entero para la cantidad.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")


# Función para ver todos los productos
def ver_productos():
    if len(productos) == 0:
        print("No hay productos en el inventario.")
    else:
        print("Lista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(
                f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}"
            )


# Función para actualizar un producto
def actualizar_producto():
    ver_productos()

    if len(productos) > 0:
        nombre_producto = input("Introduce el nombre del producto a actualizar: ")
        producto = next((p for p in productos if p["nombre"] == nombre_producto), None)

        if producto:
            print("¿Qué te gustaría actualizar?")
            print("1: Nombre")
            print("2: Precio")
            print("3: Cantidad")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre: ")
                producto["nombre"] = nuevo_nombre
                print(f"El nombre del producto ha sido actualizado a '{nuevo_nombre}'.")
            elif opcion == "2":
                while True:
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio: "))
                        producto["precio"] = nuevo_precio
                        print(
                            f"El precio del producto ha sido actualizado a {nuevo_precio}."
                        )
                        break
                    except ValueError:
                        print("Por favor, introduce un valor numérico.")
            elif opcion == "3":
                while True:
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                        producto["cantidad"] = nueva_cantidad
                        print(
                            f"La cantidad del producto ha sido actualizada a {nueva_cantidad}."
                        )
                        break
                    except ValueError:
                        print("Por favor, introduce un número entero.")
            else:
                print("Opción no válida.")
        else:
            print(f"El producto '{nombre_producto}' no fue encontrado.")


# Función para eliminar un producto
def eliminar_producto():
    ver_productos()

    if len(productos) > 0:
        nombre_producto = input("Introduce el nombre del producto a eliminar: ")
        producto = next((p for p in productos if p["nombre"] == nombre_producto), None)

        if producto:
            productos.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado correctamente.")
        else:
            print(f"El producto '{nombre_producto}' no fue encontrado.")


# Función para guardar los datos en un archivo
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(
                f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            )
    print("Datos guardados en productos.txt.")


# Función para cargar los datos desde un archivo sin usar os
def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append(
                    {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad),
                    }
                )
        print("Datos cargados desde productos.txt.")
    except FileNotFoundError:
        print(
            "No se encontró el archivo productos.txt, iniciando con un inventario vacío."
        )


# Función del menú principal
def menu():
    cargar_datos()

    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            guardar_datos()
            print("Saliendo del sistema de gestión de productos.")
            break
        else:
            print("Por favor, selecciona una opción válida.")


# Ejecutar el menú principal
menu()
