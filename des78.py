valores = []
for c in range (0,5):
    valores.append (int(input('Digite um valor: → ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'O maior valor é {max(valores)}')
print(f'O menor valor é {min(valores)}')
print(f'Cheguei ao final da lista!')