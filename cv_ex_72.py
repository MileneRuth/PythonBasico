cont = ('zero'' q','um', 'dois ','três', 'quatro','cinco', 'seis','sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'desessete', 'dezoito' , 'dessenove', 'vinte')
resp = 'S'
num = 0
while resp in 'Ss':
    if 0 <= num <= 21: 
       num = int(input('Digite um número entre 0 é 20: '))
       print(f'Você digitou o número {cont[num]}')
       resp = str(input('Quer continua? [S/N]')).upper().strip() [0]   
    else:
        break
print('obrigado por participar')
    
    

