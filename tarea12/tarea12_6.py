#funcion creamos una lista de n empleados
def crearLista(n):
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista





#funcion que crea dos listas (positivos y negativos)
def dosListas(lista):
    positivos=[]
    negativos=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])
    return [positivos,negativos]



def visualizar(positivos,negativos):
    print("Positivos:",positivos)
    print("Negativos:",negativos)


#Programa principal
lista=crearLista()
print(lista)
positivos,negativos=dosListas(lista)
visualizar(positivos,negativos)
