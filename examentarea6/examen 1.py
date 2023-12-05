n=int(input("Meses del año"))
for x in range(n):
    num=float(input("Introduce un número del 1 al 12:"))
    if num>12:
        print("Número erróneo")
    else:
        if num==4 or num==6 or num==9 or num==11:
            print("Este mes tiene 30 días")
        else:
                  if num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12:
                      print("Este mes tiene 31 días")
        if num==2:
            print ("Este mes tiene 28 días, 29 días en los años bisiestos")
