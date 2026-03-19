#Variables
inventario = []
opcion = 0

#Condicionales para validar la opción escogida
while opcion != 4:

    #Opciones a escoger
    print("-"*30)
    print("MENÚ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("-"*30)
    opcion = int(input("Ingrese el número correspondiente a la acción que desea realizar: "))

    if opcion == 1:
     c_producto = int(input("¿Cuántos productos desea agregar? "))
     for i in range(c_producto):
       nombre = input("Ingrese el nombre del producto: ")
       precio = float(input("Ingrese el precio del producto: "))
       cantidad = int(input("Ingrese cuantos productos desea comprar: "))
       if precio <= 0 and cantidad <= 0:
         print("¡Error! recuerda que el precio y la cantidad no pueden ser negativos")
         print("Introducelos de nuevo")
         precio = float(input("Ingrese el precio del producto: "))
         cantidad = int(input("Ingrese cuantos productos desea comprar: "))
       
       producto = {
        "Nombre": nombre,
        "Precio": precio,
        "Cantidad": cantidad
       }
       inventario.append(producto)
       print("¡El producto se agregó correctamente!")
       print(f"{inventario}")

    elif opcion == 2:
      if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio")
      else:
        for producto in inventario:
         print(producto)

    elif opcion == 3:
     if len(inventario) == 0:
        print("-"*30)
        print("El inventario está vacio, no hay estadisticas para calcular")
     else:
        print("Calcula la estadistica")

    elif opcion == 4:
     print("-"*30)
     print("¡Vuelva pronto!")
     break

    else:
     print("¡Opción invalida, intentelo nuevamente!")
