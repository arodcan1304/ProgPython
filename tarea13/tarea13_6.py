#Crear una lista de 5 productos

def cargar_productos():
    productos=[]
    for x in range(5):
        producto=input("Introduce el nombre del producto:")
        precio=int(input("Precio del producto:"))
        productos.append((producto,precio))
    return productos

# Visualizar los 5 productos

def visualizar_productos(productos):
    print("Listado de todos los productos")
    for producto in productos:
        print(producto[0],"tiene un precio:",producto[1])


# Visualizar los productos entre 10 y 15

def visualizar_productos_ofertas(productos):
    print("Listado de los productos entre 10 y 15")
    for producto in productos:
        prod=producto[1]
        if(prod>=10 and prod<=15):
            print(producto[0],"tiene un precio:",producto[1])

#Programa principal

productos=cargar_productos()
visualizar_productos(productos)
visualizar_productos_ofertas(productos)
