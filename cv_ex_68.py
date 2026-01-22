from random import randint
v = 0
while True:
    jogador =int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'p':
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente ? ')
print(f'GAMER OVER você venceu {v} vezes consecutivas ')
    