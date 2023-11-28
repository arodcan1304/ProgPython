positivos=0
negativos=0
mult15=0
sumaPares=0
for x in range(5):
    numero=int(input("Numero:"))
    if numero>0:
        positivos=positivos+1

    else:
        negativos=negativos+1

    if numero%15==0:
        mult15=mult15+1

    if numero%2==0:
        sumaPares=sumaPares+numero

print("Positivos:",positivos)
print("Negativos:",negativos)
print("Multiplos de 15:",mult15)
print("Suma de los pares:",sumaPares)
