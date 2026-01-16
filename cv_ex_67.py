from time import sleep
cont = n  = 0
while True:
    n = int(input('Digite um valor: '))
    print(f'A tabuado do {n}')
    sleep(2)
    if  n > 0 :
        for c in range(1,11): 
         print(f'{n} x {c} = {n*c}')
        
    else:
        break        
print('Desculpe esse valor e invalido')
          