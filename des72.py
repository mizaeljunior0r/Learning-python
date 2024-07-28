contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Insira um número →  '))
    if 0 <= numero <=20:
        print(f'Você digitou o número {contagem[numero]}.') 
        fim = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
    if fim == 'N':
        break

    else:
        print('Tente novamente!')
        numero = int(input('Insira um número →  '))
    
    print(f'Você digitou o número {contagem[numero]}.')     