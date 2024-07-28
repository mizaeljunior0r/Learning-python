val = list()

for i in range (0,5):
    n = int(input('Digite um valor → '))
    if i == 0 or n > val[-1]:
        val.append(n)
    #elif i > val[len(val)-1]:
    else:
        pos = 0
        while pos < len(val):
            if n<= val[pos]:
                val.insert(pos,n)
                print('Adicionado')
                break
            pos+=1
print('-='*30)
print(f'{val}')    