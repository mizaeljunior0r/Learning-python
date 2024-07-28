val = []
while True:
    n = int(input('Insira um valor na lista: → '))
    if n not in val:
        val.append(n)    
    else:
        print('Insira outro valor!!!') 
    cont = str(input('Deseja continuar? → ')).upper().strip()[0]   
    if cont == 'N':
        print(f'Até mais!!!')
        break
print(f'original → {val}')
val.sort()
print(f'sorted - ordenados → {sorted(val)}')
val.reverse()
print(f'reversed - reverso → {val}')
#print(f'Os valores digitados foram → {sorted(val)}') #minha opção foi usar sorted para ajustar em ordem decrescente
