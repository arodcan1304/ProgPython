cantidad=0
n=int(input("Cuantos triángulos?"))
for x in range(n):
    base=float(input("Base del triángulo:"))
    altura=float(input("Altura del triángulo:"))
    Superficie=base*altura/2
    print("El triángulo cuya base es ",base," y la altura es ",altura," tiene una superficie de ",Superficie)
    if Superficie>12:
        cantidad=cantidad+1

print("Cantidad de triangulos cuya superficie es superior a 12:",cantidad)
