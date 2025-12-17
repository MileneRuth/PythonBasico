nome = input('Qual seu nome?') 
idade = input('qual sua idade?')
if nome and idade:
    print(f'seu nome e {nome}')
    print(f'seu nome invertido e {nome[::-1]}')
    print('seu nome contém (ou não) espaços? {}'.format(" " in nome))
    print('seu nome tem {} letras'.format(len(nome.replace(" ", ""))))
    print('a primeira letra do seu nome é {}'.format(nome[0]))
    print('a ultima letra do seu nome é {}'.format(nome[-1]))
else:
    print("Desculpe, você deixou campos vazios.")