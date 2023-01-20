import pandas as pd

#Referencia : https://insightlab.ufc.br/10-funcoes-mais-usadas-para-manipular-dataframes-no-pandas

!wget 46.101.230.157/dilan/pandas_tutorial_read.csv

pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

#article_read #Toda tabela
#article_read.head() #Inicio da tabela
#article_read.tail()
#article_read.sample(5) #Randomico
#article_read[['country', 'user_id']]
#article_read['user_id'] #Coluna
#article_read[article_read.source == 'SEO'] #Filtro
#article_read.source == 'SEO' #Boolean de busca (True|False)
#article_read[['country', 'user_id']].head()

article_read.sort_values(by='user_id',ascending=False)