for numero in range(11,20):
    if numero % 2 == 0:
        print("O número par encontrado é:",numero)
        break
for numero in range(1,11):
    if numero == 5:
        continue
    print(numero)