temp = []#criando lista temporária
princ = []# lista principal que vai importar os valores.
mai = men = 0
while True:
    temp.append(str(input('Nome  → ')))
    temp.append(float(input('peso → ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
         if temp[1] > mai:
            mai = temp[1]
         if temp[1] < men:
             men = temp[1]       
    princ.append(temp[:])#criando cópia da lista
    temp.clear()#limpando a lista principal
    resp = str(input('terminar? '))
    if resp  in 'sS':
        break
print('-='*30)
print(f'Você cadastrou → {len(princ)}')
print(f'O maior peso foi de {mai} kg.')
for p in princ:
    if p [1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi fe {men} kg')
for j in princ:
    if j [1] == men:
        print(f'{j[0]}')