print('Calculador de PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da Pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}->'.format(termo), end='')
        termo += razão
        cont += 1 
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progreção finalizado com {} termosmostrado'.format(total))