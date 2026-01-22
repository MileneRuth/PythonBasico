'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário ue ou não continuar no final, mostre 
a) quantas pessoas tem 18 anos 
b) quantos homens foram cadastrados 
c) quantas mulheres tem menos de 20 anos'''
id = sex = cont = 0
print('Olá preciso de algumas informações para cadastro')
while True:
    idade = int(input('poderia me informa a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('poderia me informa o Sexo:[F/M] ')).strip().upper()[0]
        if idade >= 18:
            id += 1
        if sexo =='M':
            sex += 1
        if sexo == 'F' and idade < 20:
            cont +=1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('gostaria de continua? [S/N] ')).strip().upper()[0]
    if opção == 'N':
         break
print( f'Muito obrigado,\n Tivemos o total de {id} pessoas com 18 anos \n O total de homens cadastrados foi de {sex} \n Mulheres com menos de 20 anos temos {cont}')

   
    