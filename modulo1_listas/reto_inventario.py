# reto modulo 1 - listas
# sistema de inventario con listas anidadas
# cada producto es una lista: [nombre, cantidad, precio]

inventario = [
    ["Laptop", 10, 1200.00],
    ["Teclado", 25, 45.00],
    ["Mouse", 30, 20.00],
    ["Monitor", 8, 350.00],
    ["Auriculares", 15, 80.00]
]

# busca el producto y cambia su precio
def actualizar_precio(inventario, nombre, nuevo_precio):
    encontrado = False
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            print(f"precio anterior de {nombre}: ${producto[2]}")
            producto[2] = nuevo_precio
            print(f"nuevo precio: ${producto[2]}")
            encontrado = True
    if not encontrado:
        print(f"{nombre} no esta en el inventario")

# descuenta del stock si hay suficiente
def registrar_venta(inventario, nombre, cantidad):
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            if producto[1] >= cantidad:
                producto[1] -= cantidad
                total = cantidad * producto[2]
                print(f"venta de {cantidad} {nombre} por ${total:.2f} - stock actual: {producto[1]}")
            else:
                print(f"no hay suficiente stock de {nombre}, solo hay {producto[1]}")
            return
    print(f"{nombre} no encontrado")

# agrega producto nuevo o suma stock si ya existe
def aniadir_producto(inventario, nombre, cantidad, precio=0):
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            producto[1] += cantidad
            print(f"se agrego stock a {nombre}, total ahora: {producto[1]}")
            return
    inventario.append([nombre, cantidad, precio])
    print(f"producto nuevo agregado: {nombre}")

# muestra todo el inventario
def mostrar_inventario(inventario):
    print("\n---- inventario actual ----")
    print(f"{'producto':<15} {'cantidad':>10} {'precio':>10} {'total':>10}")
    print("-" * 50)
    for producto in inventario:
        nombre, cantidad, precio = producto
        total = cantidad * precio
        print(f"{nombre:<15} {cantidad:>10} {precio:>10.2f} {total:>10.2f}")
    print("-" * 50)

# programa principal
print("=== sistema de gestion de inventario ===\n")

print("inventario inicial:")
mostrar_inventario(inventario)

print("\nactualizando precios:")
actualizar_precio(inventario, "Laptop", 1099.99)
actualizar_precio(inventario, "Monitor", 320.00)
actualizar_precio(inventario, "Webcam", 60.00)

print("\nregistrando ventas:")
registrar_venta(inventario, "Teclado", 5)
registrar_venta(inventario, "Mouse", 35)
registrar_venta(inventario, "Laptop", 3)

print("\nagregando productos:")
aniadir_producto(inventario, "Mouse", 20)
aniadir_producto(inventario, "Webcam", 10, 65.00)

print("\ninventario final:")
mostrar_inventario(inventario)