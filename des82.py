lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Informe um número →     ')))
    fim = str(input('Deseja finalizar? →        '))  
    if fim == 's':
        print('Obrigado por participar')
        break
for i, v in enumerate (lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'-='*30)
print(f'Lista original → {lista}')
print(f'Lista par → {pares}')
print(f'Lista par → {impares}')
print('Fim')