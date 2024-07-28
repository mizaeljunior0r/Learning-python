prod = ('lápis','Borracha','caderno','estojo','transferidor','compasso','mochila','canetas','Livro')
preco = (2.10,50,11,9.10,2.30,6.10,7.50,8.20,9.90)
jun = prod + preco
#print(jun)
for c, d in zip(prod,preco):
    print(f'{c:.<30}',end='')
    print(f'R$ {d:.2f}')
    
    