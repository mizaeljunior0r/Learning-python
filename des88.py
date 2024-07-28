from random import randint

tp = []
palpite = int(input('Quantos jogos vai fazer? → '))

for j in range (palpite):
    jogo = []
    while len (jogo) < 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    tp.append(sorted(jogo))        

print('#'*30)
for jogo in tp:    
    print(jogo)