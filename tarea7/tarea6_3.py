"""Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética"""

#Introducir los tres nombres
nombre1=input("Primer nombre:")
nombre2=input("Segundo nombre:")

if nombre1>nombre2:
    print(nombre2," ",nombre1)
else:
    print(nombre1," ",nombre2)
