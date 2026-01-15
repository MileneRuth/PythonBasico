import random
n = cont = opção = 0
print('Jogo do Par ou Impar')
while True:
    n = int(input('Digite um numero: '))
    cl = str(input('E agora escolha uma opção [par] ou [impar] ? ')).lower
    pc = random.randint(0,11)
    print(f'O computador escolheu {pc}')
    soma = n + pc 
    if soma % 2 == 0:
        opção = ['par']
        print('Parabens você ganhou')
        cont += 1
    else:
        break
print(f'Fim você perdeu e teve o total de {cont} vitorias ')
    
    