num = (int(input('Insira um número:  → ')), int(input('Insira um número:  → ')), int(input('Insira um número:  → ')), int(input('Insira um número:  → ')), int(input('Insira um número:  → ')))
print(f'Os números digitados foram: {num}')
print(f'O numero 9 apareceu:    {num.count(9)}x')
if 3 in num:
    print(f'A posição em que foi digitado o primeiro valor 3 é a:   {num.index(3) + 1}')
else:
    print('O valor 3 não foi digitado!')
print('Os numeros pares foram → ',end='')    
for n in num:
    if n % 2 == 0:
        print(f' {n} ', end='')
        
