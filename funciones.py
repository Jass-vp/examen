productos={'8475HD':['HP',15.6,'8GB','DD','1T','Intel core i5','Nvidia GTX1050'],
           '2175HD':['lenovo',14,'4GB','SSD','512GB','Intel core i5','Nvidia GTX1050'],
           'JjfFHD':['Asus',14,'16GB','SSD','256GB','Intel core i7','Nvidia RTX2080Ti'],
           'fgdxFHD':['HP',15.6,'8GB','DD','1T','Intel core i3','integrada'],
           'GF75HD':['Asus',15.6,'8GB','DD','1T','Intel core i7','Nvidia GTX1050'],
           '123FHD':['lenovo',14,'6GB','DD','1T','AMD Ryzer 5','integrada'],
           '342FHD':['lenovo',15.6,'8GB','DD','1T','AMD Ryzer 7','Nvidia GTX1050'],
           'UWU131HD':['Dell',15.6,'8GB','DD','1T','AMD Ryzer 3','Nvidia GTX1050'],}

stock={'8475HD':[387990,10],'2175HD':[327990,4],'JjfFHD':[424990,1],
       'fgdxHD':[664990,21],'123FHD':[290890, 32],'342FHD':[444990,7],
       'GF75HD':[749990,2],'UWU131HD':[349990, 1],'FS1230HD':[249990,0],}

def stock_marca (marca):
    for id_producto in productos:
        if productos[id_producto][0].lower()==marca:
            if id_producto in stock and len(stock[id_producto])>1:
                print("El stock",marca, "es:",stock[id_producto][1])

"""def busqueda (precio_min,precio_max):
    lista=[]
    for id_producto in productos:
        precios= stock[id_producto][0]
        if id_producto in stock and len(stock[id_producto])>1:
            stock_marca=productos[id_producto][0]
            if precio_min <= precios <= precio_max and stock_marca >0:
                marca=productos[id_producto][0]
                lista.append(f"{marca}-{stock[id_producto]}")
            if not lista:
                print("No se encuentran productos dentro de ese precio")
            else:
                lista.sort()
                print("Los productos son",lista)"""
def busqueda(precio_min, precio_max):
    lista = []

    for id_producto in productos:
        if id_producto in stock and len(stock[id_producto]) > 1:
            precio = stock[id_producto][0]
            cantidad = stock[id_producto][1]
            if precio_min <= precio <= precio_max and cantidad > 0:
                marca = productos[id_producto][0]
                lista.append(f"{marca} - {id_producto} - ${precio} - {cantidad} unidades")

 
    if not lista:
        print("No se encuentran productos dentro de ese precio.")
    else:
        lista.sort()
        print("Los productos son:")
        for item in lista:
            print(item)
def actualizar (producto_id, nuevo_precio):
    if producto_id in stock:
        if len(stock[producto_id])==0:
            stock[producto_id]=[0,nuevo_precio]
        else:
            stock[producto_id][0]=nuevo_precio
            return True
    else:
        return False
