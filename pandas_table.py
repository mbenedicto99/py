'''
TABELAS
'''

import pandas as pd

Medalhas_Rio2016 = {
    'País': ['USA', 'Grã-Bretanha', 'China', 'Rússia', 'Alemanha', 'Japão', 'França', 'C. do Sul', 'Itália', 'Austrália', 'Brasil'],
    'Ouro': [46, 27, 26, 19, 17, 12, 10, 9, 8, 8, 7],
    'Prata': [37, 23, 18, 18, 10, 8, 18, 3, 12, 11, 6],
    'Bronze': [38, 17, 26, 19, 15, 21, 14, 9, 8, 10, 6]}


olimpiadas_rio2016 = pd.DataFrame (Medalhas_Rio2016)

#TABELA
#print (olimpiadas_rio2016)

#MOSTRA TAMANHO DE LINHAS E COLUNAS
#print (olimpiadas_rio2016.shape)

#MOSTRA CABEÇALHO
#print (olimpiadas_rio2016.columns)

#CRIA COLUNA DE TOTAL
olimpiadas_rio2016['Total'] = olimpiadas_rio2016['Ouro'] + olimpiadas_rio2016['Prata'] + olimpiadas_rio2016['Bronze']
#print (f'{olimpiadas_rio2016}')

#RENAME COLUMN
olimpiadas_rio2016.rename(columns={'Total':'Total_Medalhas'}, inplace=True)
#print (f'{olimpiadas_rio2016}')

#REMOVE COLUNAS
olimpiadas_rio2016.drop(['Ouro'], inplace=True, axis=1)
#print (f'{olimpiadas_rio2016}')

#CORTE NA TABELA - ATE LINHA :3
#print (f'{olimpiadas_rio2016[:3]}')

#CORTE NA TABELA POR LINHA (ILOC e LOC)
#print (f'{olimpiadas_rio2016.iloc[[3,6], [1,3]]}') # APENAS LINHAS 3 e 6
#print (f"{olimpiadas_rio2016.loc[[4,9], ['Prata', 'Bronze']]}")  # APENAS LINHAS 4 e 9 MUDANDO HEADER

#MODO APPLY

#print (olimpiadas_rio2016.loc[0:2, ['País', 'Prata']].apply(lambda x: print(x), axis = 1)) # AXIS=EIXO (1=linha e 0=coluna) APPLY aplica uma função a cada elemento
print (olimpiadas_rio2016.loc[0:2, ['País', 'Prata']].apply(lambda x: print(x), axis = 0))

