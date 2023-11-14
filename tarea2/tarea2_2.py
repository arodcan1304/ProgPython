nota1=int(input("Introduce la primera nota:"))
nota2=int(input("Introduce la segunda nota:"))
nota3=int(input("Introduce la tercera nota:"))

suma=nota1+nota2+nota3

media=suma//3


if media>=5: 
    print("El alumno ha aprobado con una media de ",media)


else:
    print("El alumno ha suspendido con una media de ",media)
