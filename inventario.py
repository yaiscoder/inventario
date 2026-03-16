print("¡Bienvenido al sistema de inventario!")
opcion = "yes"

while opcion == "yes":
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: $ "))
    cantidad=int(input("Ingrese la cantidad del producto:  "))

    if precio < 0:
        print("Error: El precio y la cantidad deben ser números positivos.ejemplo(1, 2, 3...)")
        print("Por favor, ingrese un precio válido.")
    elif cantidad < 0:
        print("Error: El precio y la cantidad deben ser números positivos.(ejemplo: 1, 2, 3...)")
        print("Por favor, ingrese una cantidad válida.")
        break


    else:
        costo_total=precio*cantidad
        print("El total del inventario es: $", costo_total)
                

        print(f"nombre del producto: {nombre}")
        print(f"precio del producto: $ {precio}")
        print(f"cantidad del producto: {cantidad}")
        print(f"costo total: $ {costo_total}")
        break


