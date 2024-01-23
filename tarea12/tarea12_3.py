# función que crea una lista de n elementos

def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

# función que devuelve el producto de sus elementos
def producto(lista):
    p=1
    for x in range(len(lista)):
        p=p*lista[x]
    return p


# Programa principal

lista=crearLista()
print(lista)
print("El producto de sus elementos es:",producto(lista))
