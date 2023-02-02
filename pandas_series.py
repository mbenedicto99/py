'''
PANDAS SERIES
'''

import pandas as pd

sr1 = pd.Series(['Espirito Santo', 'Minas Gerais', 'Sao Paulo', 'Rio de Janeiro'])
print (sr1)

dados = {
    'col1': ['Manuela', 'Dayane', 'Fernanda', 'Bia'],
    'col2': [24.0, 21.5, 19.0, 20.0],
    'col3': [1.56, 1.52, 1.53, 1.62]
}

df = pd.DataFrame(dados)
print (df)