n=int(input("Triangulos?"))
equilatero=0
isosceles=0
escaleno=0
for x in range(n):
    lado1=float(input("Lado 1:"))
    lado2=float(input("Lado 2:"))
    lado3=float(input("Lado 3:"))
    if lado1==lado2 and lado1==lado3:
        print("Triángulo equilátero")
        equilatero=equilatero+1

    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Triángulo isósceles")
            isosceles=isosceles+1
        else:
            print("Triángulo escaleno")
            escaleno=escaleno+1

print("Cantidad de equilateros:",equilatero)
print("Cantidad de isosceles:",isosceles)
print("Cantidad de escaleno:",escaleno)
