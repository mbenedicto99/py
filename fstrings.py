'''
##INTERPOLACAO
nome = 'Joao'
preco = 1000.2323
variavel = '%s, o preco é R$%.2f' % (nome, preco)

print (variavel)
print ('%d e %08X' % (1500, 1500))
'''

#FSTRINGS
var = "ABC"
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}.')
print(f'{var: ^10}.')
print(f'{12813.1231231:,.2f}')