palavras = ('pombo', 'ganso', 'cavalo','morcego','jumento','golfinho')
for p in palavras:
    print(f'\n Na palavra {p} temos as vogais',end='')
    for letra in p:
        if letra in 'aeiou':
            print(f' {letra}',end='')