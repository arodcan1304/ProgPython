from math import sqrt
a=int(input("Introduce coeficiente a:"))
b=int(input("Introduce coeficiente b:"))
c=int(input("Introduce coeficiente c:"))
aux=b*b-4*a*c
if aux<0:
    print("Soluciones complejas")
else:
    raiz(sqrt(aux))
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    print("Solucion 1:" ,x1)
    print("Solucion 2:" ,x2)
