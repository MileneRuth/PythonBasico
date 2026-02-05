'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuários qual será o valor a ser sacado ( número inteiro ) e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS só considere que o caixa possui cédulas de R$ 50 , 20, 10 e 1. 
'''
print('Banco da MIMI')
print('So temos notas de R$50, R$20, R$10 e R$1')
valor = int(input('Digite valor a ser sacado R$: '))
nota = 50
totnota = 0
while True:
    if valor >= nota:
        valor -= nota
        totnota += 1
    else:
        print(f'Total de {totnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if valor == 0:
            break
print('Tchau')