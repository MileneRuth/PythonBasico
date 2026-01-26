'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuários qual será o valor a ser sacado ( número inteiro ) e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS só considere que o caixa possui cédulas de R$ 50 , 20, 10 e 1. 
'''
print('Banco da MIMI')
print('So temos notas de R$50, R$20, R$10 e R$1')
nota = 50
while True:
    valor = int(input('Digite valor a ser sacado R$: '))
    soma = nota / valor
    if soma == 2:
        five +=1
        if soma < 20:
            vintao +=1
            if soma < 10:
                ten +=1
                if soma < 1:
                    one +=1
                else:
                    break
print(' Retire os seguintes valores no ghiche {five} notas de R$50 e {vintao} notas de R$20 e {ten} notas de R$10, e por fim {one}notas de 1 real, somando os {valor}')