# Definir lista vacía
lista1=[]
lista2=[]
lista3=[]
# Agregamos 4 numeros a lista1 y lista2
for x in range(4):
    nom=int(input("Ingrese un número a la lista 1:"))
    lista1.append(nom)
    nom=int(input("Ingrese un número a la lista 2:"))
    lista2.append(nom)
    
# Sumar ambas listas

for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)

# Visualizar lista suma

print("La lista resultante:", lista3)
  
