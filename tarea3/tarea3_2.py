nota=int(input("Introduce una nota:"))
if nota<5:
    print("Suspenso")
else:
    if nota<6:
        print("Aprobado")
    else:
        if nota<7:
            print("Bien")
        else:
                    if nota<9:
                        print("Notable")
                    else:
                        print("Sobresaliente")
