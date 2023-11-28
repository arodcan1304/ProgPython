turno1=0
turno2=0
turno3=0
print("Turno de mañana:")
for x in range(5):
    edad=int(input("Edad:"))
    turno1=turno1+edad
print("Turno de tarde:")
for x in range(6):
    edad=int(input("Edad:"))
    turno2=turno2+edad
print("Turno de noche:")
for x in range(11):
    edad=int(input("Edad:"))
    turno3=turno3+edad
promedio1=turno1/5
promedio2=turno2/6
promedio3=turno3/11
print("Edad de la mañana",promedio1)
print("Edad de la tarde",promedio2)
print("Edad de la noche",promedio3)
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de mañana tiene mayor promedio de edad")
else:
    if promedio2>promedio3:
        print("El turno de tarde tiene mayor promedio de edad")
    else:
        print("El turno de noche tiene mayor promedio de edad")
