total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1 
    total += preço
    if preço < 1000:
        totmil +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp =' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continua? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40} Fim do programa ')
print(f'O total da compra foi de {total}')
print(f'Temos {totmil} produtos que custam mais de 1.000,00 reais')
print(f'O produto mais barato foi {barato} que custou R${menor}')