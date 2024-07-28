from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for n in numeros: 
    print(f'{n} → ', end='') #se eu mandar printar o numeros, ele vai printar todos os numeros 5x, mas se mandar printar o n vai ficar 5 numeros aleatórios 
print(f'\n  O maior Valor sorteado foi: {max(numeros)}')
print(f'  O menor valor sorteado foi: {min(numeros)}')
    
    
  



    