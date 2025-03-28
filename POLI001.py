# ESTUDOS ESCOLA POLITECNICA

# Finalidade  : Estudo de Algebra Linear
# Autor       : Marcos de Benendicto (AI)
# Data        : 28/03/2025

"""1. Álgebra Linear e Geometria Analítica
Contexto:
Fundamenta o estudo de espaços vetoriais e transformações lineares, essenciais para modelagem matemática em diversas áreas, como engenharia, IA e estatística.
📘 Tópicos:
Vetores, matrizes
Sistemas lineares
Espaços vetoriais
Produtos interno, norma, ortogonalidade
Geometria no plano e espaço
🛠️ Exemplo prático:
Calcular o trajeto ideal de um drone em um ambiente 3D evitando obstáculos, utilizando vetores, planos e projeções."""

import numpy as np

# Produto escalar
v1 = np.array([1, 2])
v2 = np.array([3, 4])
dot_product = np.dot(v1, v2)  # Resultado: 11

# Produto matricial
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
C = np.dot(A, B)

-------------------------------------------------
#2. Decomposição de Valor Singular (SVD)

"""Contexto:
Método de fatoração de matrizes útil para compressão de dados, redução de dimensionalidade e extração de padrões.
🛠️ Exemplo prático:
Compressão de imagens: reduz a quantidade de dados armazenados preservando a qualidade visual. O JPEG usa SVD."""

# SVD de uma matriz
A = np.array([[1, 2], [3, 4], [5, 6]])
U, S, VT = np.linalg.svd(A)

# Reconstrução
S_mat = np.zeros((3, 2))
S_mat[:2, :2] = np.diag(S)
A_reconstructed = U @ S_mat @ VT

-------------------------------------------------
#3. Otimização (Gradiente Descendente)

"""Contexto:
Busca encontrar o melhor resultado possível (mínimo ou máximo) para um determinado problema, com ou sem restrições.
📘 Tópicos:
Derivadas e derivadas parciais
Gradiente, Hessiana, Jacobiano
Algoritmos de gradiente descendente
Problemas convexos e não convexos"""

# Minimizar f(w) = (w - 3)^2
w = 0.0
alpha = 0.1

for i in range(20):
    grad = 2 * (w - 3)
    w = w - alpha * grad

# w converge para 3

-------------------------------------------------
#4. Estatística Descritiva

"""Contexto:
Analisa e resume dados (descritiva) e realiza inferências sobre populações com base em amostras (indutiva).
📘 Tópicos:
Média, mediana, moda
Variância, desvio padrão
Gráficos e histogramas
Estimação de parâmetros"""

import pandas as pd

data = [10, 20, 20, 30, 40]
df = pd.Series(data)

media = df.mean()
mediana = df.median()
desvio_padrao = df.std()

-------------------------------------------------
#5. Probabilidade e Teorema de Bayes

"""Avalia incertezas e a chance de ocorrência de eventos, essencial para análise preditiva.
📘 Teorema de Bayes:
"""

# Teorema de Bayes
P_Dado_Positivo = 0.99
P_Pos = 0.01 * 0.99 + 0.99 * 0.05
P_Doenca_dado_Pos = (0.99 * 0.01) / P_Pos  # Resultado ~0.17

-------------------------------------------------
#6. Modelos de Probabilidade

"""Contexto:
Modelam fenômenos aleatórios. Discretos lidam com contagens, contínuos com medições.
📘 Exemplos:
Discreto: Binomial, Poisson
Contínuo: Normal, Exponencial
🛠️ Exemplo prático:
Modelar a quantidade de veículos que chegam por minuto a um pedágio (Poisson)."""

from scipy.stats import poisson, norm

# Poisson: probabilidade de 3 carros/min, média=2
p = poisson.pmf(3, mu=2)

# Normal: probabilidade de X < 1.8, média=2, desvio=0.5
p_norm = norm.cdf(1.8, loc=2, scale=0.5)

-------------------------------------------------
#7. Intervalo de Confiança e Teste de Hipóteses

"""Contexto:
Determina estimativas para parâmetros populacionais e testa hipóteses com base em dados amostrais.

📘 Fórmulas:
Intervalo de Confiança:
Exemplo prático:
Avaliar se a nova política de tráfego da CCR reduziu significativamente o tempo médio de viagem."""


from scipy import stats
import numpy as np

amostra = np.array([12, 15, 14, 10, 13])
media = np.mean(amostra)
n = len(amostra)
sem = stats.sem(amostra)
conf_int = stats.t.interval(0.95, df=n-1, loc=media, scale=sem)

-------------------------------------------------
#8. Modelos de Markov

"""Contexto:
Modelos estocásticos usados para prever sistemas que evoluem ao longo do tempo, onde o futuro depende apenas do estado atual.
📘 Equação de transição:
# Matriz de transição de estados do trânsito
🛠️ Exemplo prático:
Prever o estado de tráfego (livre, moderado, congestionado) com base nos estados anteriores."""

import numpy as np

P = np.array([
    [0.7, 0.2, 0.1],  # estado livre
    [0.3, 0.4, 0.3],  # estado moderado
    [0.2, 0.3, 0.5]   # estado congestionado
])

estado_inicial = np.array([1, 0, 0])  # Começa livre
estado_futuro = estado_inicial @ P @ P  # Após 2 passos

