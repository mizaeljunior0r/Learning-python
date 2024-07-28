dados = []
while True:
    dtemp = [[],[],[],[]]
    nome = str(input('Informe o seu nome → '))
    nota1 = float(input('Informe sua primeira nota → '))
    nota2 = float(input('Informe sua segunda nota → '))
    med = nota1 + nota2 / 2
    fim = str(input('Deseja terminar?'))
    dtemp[0].append(nome)
    dtemp[1].append(nota1)
    dtemp[2].append(nota2)
    dtemp[3].append(med)
    dados.append(dtemp[:])
    dtemp.clear()
    if fim not in 'Nn':
        break
#print(f'Lista final{dados}')
for t in dados:
    print(f'{t([0])}')