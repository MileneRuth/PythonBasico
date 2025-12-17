#nome = 'milene ruth'
#altura = 1.50
#peso = 70
#imc = peso / (altura ** 2)
#print(nome, '\ntem', altura, 'de altura,\n pesa', peso,'quilos e seu imc é de', imc)

nome = 'milene ruth'
altura = 1.50
peso = 70
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:,.2f} de altura,'
linha_2 = f' pesa {peso} quilos e seu imc é de {imc:,.2f}'
print(linha_1, linha_2)