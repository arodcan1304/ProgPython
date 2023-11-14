num=int(input("Introduce un número de 1 o dos dígitos:"))
if num>0:
    if num<100:
        if num>=10:
            print("El número tiene dos cifras")

        else:
            print("El número tiene una cifra")

    else:
        print("El número tiene más de dos cifras")


else:
    print("El número es negativo")
