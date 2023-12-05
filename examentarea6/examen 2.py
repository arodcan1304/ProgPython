def contar_cifras():
    n=int(input("Introduce un número entero: "))
    numero_absoluto=abs(n) 
    cifras=1
    while numero_absoluto // 10 > 0:
        cifras += 1
        numero_absoluto=numero_absoluto // 10
    print("El número ",n," tiene ",cifras," cifras.")

contar_cifras()
