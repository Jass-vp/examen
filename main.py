import funciones as fn
op=0
while op !=4:
    print("""
          ***MENU PRINCIPAL***
          1.- Stock marca
          2.- Búsqueda por precio
          3.- Actualizar precio
          4.- Salir""")
    try:
        op=int(input("Ingrese la opción deseada: "))
    except ValueError:
        print("Ingrese una opción valida")
        continue
    if op==1:
        marca=input("Ingrese la marca que desea buscar: ").lower()
        fn.stock_marca(marca)

    elif op==2:
        while True:
            try:
                precio_min=int(input("Ingrese el precio minímo de busqueda: "))
                precio_max=int(input("Ingrese el precio maximo para la busqueda: "))
                break
            except ValueError:
                print("Debe ingresar un número valido")
                fn.busqueda(precio_min,precio_max)
    elif op ==3:
        while True:
            producto_id=input("Ingrese la ID del producto que desea cambiar su valor: ")
            try:
                nuevo_precio=float(input("Ingrese el precio que desea asignarle: "))
                actualizar=fn.actualizar(producto_id,nuevo_precio)
                if actualizar :
                    print("Precio actualizado")
                else:
                    print("Producto no existe")
            except ValueError:
                print("Debe ingresar un número valido")
            repetir=input("Desea actualizar otro precio? (s/n)").lower
            if repetir =="s":
                break
    
    elif op ==4:
        print("Programa finalizado")
    else:
        print("Ingrese una opción valida ")
