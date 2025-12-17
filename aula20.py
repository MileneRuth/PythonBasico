pri_valor= input('Digite o 1° valor: ')
seg_valor= input('Digite o 2° valor: ')
if pri_valor > seg_valor:
    print(f'O maior valor é {pri_valor}')
elif seg_valor > pri_valor:
    print(f'O maior valor é {seg_valor}')
else:
    print('valores iguais')
