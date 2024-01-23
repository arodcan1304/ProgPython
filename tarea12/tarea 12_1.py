# función que crea una lista de n elementos

def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

# función que multiplica los elementos de una lista por un valor
def multiplicar(lista,n):
    for x in range(len(lista)):
        lista[x]=lista[x]*n
    return(lista)


# Programa principal

lista=crearLista()
print(lista)
n=int(input("Multiplicando:"))
multiplicar(lista,n)
