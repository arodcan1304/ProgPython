# Definir lista vacia
listaM=[]
listaT=[]
# Agregamos 4 sueldos a cada lista
for x in range(4):
    valor=float(input("Introduce un sueldo de la mañana:"))
    listaM.append(valor)

for x in range(4):
    valor=float(input("Introduce un sueldo de la tarde:"))
    listaT.append(valor)

#Visualizar ambas listas

print("Sueldos de la mañana:")
print(listaM)
print("Sueldos de la tarde:")
print(listaT)

