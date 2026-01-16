'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continua, No final, mostre 
a) qual e o total gasto na compra 
b) quantos produtos custam mais de R$1000
c) Qual e o nome do produto mais barato '''
tot = cont = total = menor = 0
print('mercadinho da Ruth')
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite agora o Preço do produto R$: '))
    cont =+ 1
    total  += valor
    if valor > 1000:
         tot += 1
    if cont == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua? [S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi de {total:.2f}')
print(f'Temos {tot} produtos  que custa mais de R$ 1.000,00.')
print(f'O produto mais barato custa R${menor:.2f}')
