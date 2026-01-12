import random
n = cont = 0
print('Jogo do Par ou Impar')
while True:
    n = int(input('Digite um numero: '))
    opção = ['par']['impar'].upper().strip()
    cl = str(input('E agora escolha uma opção par ou impar ?'))
    pc = random
    if n != 0:
        if n + pc / 2 % 0:
            if opção == 'par'.upper().strip():
                print('Ganhou parabens hihi')
            elif n + pc / 2 % 1:
                if opção == 'impar'.upper().strip():
                    print('ganhou')
            cont =+1 
        else:               
                break
print(f'game over você ganhou {cont} vezes')

    