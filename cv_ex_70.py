'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continua, No final, mostre 
a) qual e o total gasto na compra 
b) quantos produtos custam mais de R$1000
c) Qual e o nome do produto mais barato '''
tot = valorb = val = cont = 0
print('mercadinho da Ruth')
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite agora o Preço do produto R$: '))
    tot += valor
    tot += 1
    if valor > 1000:
            val += 1
            if valor < valorb:
                  cont += 1
            