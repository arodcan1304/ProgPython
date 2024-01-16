# Definir lista vacía
nombres=[]
notas=[]
# Agregamos 10 nombres y notas
for x in range(10):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese una nota:"))
    notas.append(ed)

# Visualizar Suspensos y Aprobados

print("Alumnos aprobados:")
for x in range(10):
    if notas[x]>=5:
        print(nombres[x],"",notas[x])

print("Alumnos suspensos:")
for x in range(10):
    if notas[x]<5:
        print(nombres[x],"",notas[x])
