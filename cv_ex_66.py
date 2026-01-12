n = soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'o total de número digitados foram {cont} e a soma entre eles e  {soma}')

