e1 = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range (0,3):
    for c in range (0,3):
       e1[l][c] = int(input(f'digite um valor para a posição [{l},{c}]: '))

print(f'*'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{e1[l][c]}]',end='')
        if e1 [l][c] %2 == 0:
            spar += e1[l][c]
    print()
print(f'*'*30)
print(f'A soma dos valores pares é → {spar}')
for l in range (0,3):
    scol += e1[l][2]
print(f'A soma dos valores da coluna 3 é → {scol}')
for c in range (0,3):
    if c == 0:
        mai += e1[1][c]
    elif e1 [1][c] > mai:
        mai = e1[1][c]
print(f'O maior valor da segunda linha é {mai}')


