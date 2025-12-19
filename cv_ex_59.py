from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0 
while opção != 5:   
    print(''' Menu
        [1] somar
        [2] multiplicar
        [3] maior 
        [4] novos números
        [5] sair: ''' )
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} = {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2 :
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando')
    else:
        print('opção invalida,tente novamente')
    print('+=+'*10)
    sleep(2)

print('Fim ')
