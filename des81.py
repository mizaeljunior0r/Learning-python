l = []
c = 0
while True:
    l.append(int(input('Insira um valor → ')))
    cont = str(input('Continua?     ')).upper().strip()[0]
    if cont != 'S':
        break
print(f'Quantidade de Numeros digitados →       {len(l)}')
l.sort(reverse=True)
print(f'Ordenados de forma decrescente →        {l}')
print(f'Quantidade de aparições do nº 5 →       {l.count(5)}')
