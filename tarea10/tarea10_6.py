# Definir lista vacía
lista1=[]

# Agregamos 10 numeros a lista1
for x in range(10):
    nom=int(input("Ingrese un número a la lista 1:"))
    lista1.append(nom)
    
# Ordenamos la lista
for i in range(1,10):
    for j in range(10-i):
        if lista1[j]>lista1[j+1]:
            aux=lista1[j]
            lista1[j]=lista1[j+1]
            lista1[j+1]=aux

# Visualizamos la lista ordenada

print("La lista ordenada:", lista1)
  
