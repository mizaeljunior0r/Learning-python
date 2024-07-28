princ = [[],[]]
for i in range (0,7):
    i = int(input('informe um número → '))
    if i % 2 == 0:
        princ[0].append(i)
    else:
        princ[1].append(i)
print('@'*30)
princ[0].sort()
princ[1].sort()
print(f'{princ[0]}')
print(f'{princ[1]}')
        