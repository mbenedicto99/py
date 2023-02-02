'''
MATRIZES
'''

import numpy as np

A = np.array([[1,0], [0,1]])
B = np.array([[1,2], [3,4]])

mtr_linhas = np.sum(B, axis=0, keepdims=True)
mtr_colunas = np.sum(B, axis=1, keepdims=True)
mtr_soma = A + B

print(f'{mtr_linhas=}')
print(f'{mtr_colunas=}')
print(f'{mtr_soma=}')

