tbras = ('Botafogo','Palmeiras','Flamengo','São Paulo','Bahia','Cruzeiro','Fortaleza','Athletico-PR','Chapecoense','Bragantino','Atlético-MG','Juventude','Internacional','Criciúma','Cuiabá','Vitória','Corinthians','Grêmio','Atlético-GO','Fluminense')
print('-='*15)
print(f'Os 5 primeiros times → {tbras[0:5]}')
print('-='*15)
print(f'Os 4 ultimos são {tbras[-4:]}')
print('-='*15)
print(f'Os times em ordem alfabética → {sorted(tbras)}') #sorted mostra tupla ordenada
print('-='*15)
print(f'O chapecoense está na posição {tbras.index('Chapecoense')+1}ª ')
