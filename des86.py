e1 = [[0,0,0],[0,0,0],[0,0,0]]

for l in range (0,3):
    for c in range (0,3):
       e1[l][c] = int(input(f'digite um valor para a posição [{l},{c}]: '))

print(f'*'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{e1[l][c]}]',end='')
    print()