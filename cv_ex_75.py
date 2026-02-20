num = (int(input('Digite um valor : ')),
       int(input('Digite um valor : ')),
       int(input('Digite um valor : ')),
       int(input('Digite um valor : ')))
print(f'Você digitu o os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1} posição')
else:
    print('Não foi digitado em nenhuma posição')
print(f'Os vlores pares digitados foram', end= ' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
