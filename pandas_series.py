'''
PANDAS SERIES
'''

import pandas as pd

sr1 = pd.Series(['Espirito Santo', 'Minas Gerais', 'Sao Paulo', 'Rio de Janeiro'])
print (sr1)

dados = {
    'nome': ['Elisangela', 'Dayane', 'Fernanda', 'Bia'],
    'idade': [24.0, 25.0, 19.0, 20.0],
    'altura': [1.56, 1.52, 1.53, 1.62]
}

df = pd.DataFrame(dados)
print (df)