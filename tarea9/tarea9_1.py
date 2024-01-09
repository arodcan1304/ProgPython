# Definir lista vacia
lista=[]
# Agregamos 8 elementos
for x in range(8):
    valor=int(input("Introduce un número:"))
    lista.append(valor)
# Calculamos cuantos numeros son mayores a 100
contador=0
for x in range(8):
    if lista[x]>100:
        contador=contador+1

# Visualizar los datos
print(lista)
print("Mayores que 100:",contador)
