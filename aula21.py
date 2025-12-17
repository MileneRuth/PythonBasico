entrada = input('[E]ntrar [S]air: ').lower()
senha_digitada = input('Digite a senha: ')
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('sair')