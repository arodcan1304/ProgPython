# Definir lista vacia
lista=[]
# Agregamos 5 elementos
for x in range(5):
    valor=int(input("Introduce un número:"))
    lista.append(valor)
# Visualizar los mayores o iguales a 7
for x in range(5):
    if lista[x]>7:
        print(lista[x],end="")
