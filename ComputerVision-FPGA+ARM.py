"""
# Finalidade  : MLP com 4 entradas, 3 neurônios ocultos e 2 saídas
# Autor       : Marcos de Benedicto (IA)
# Data        : 22/03/2025
# Input       : 
# Output      :
Entrada X: [ 1.   0.5 -1.5  2. ]
Ativação camada oculta: [1.85  0.35  0.565]
Saída Y: [0.93  0.363]

Simularemos o produto 𝑌=𝑓(𝑊⋅𝑋)
Y=f(W⋅X), como no bloco (b) da imagem.
A função de ativação será ReLU (representando um processamento simples no FPGA).
Os pesos 𝑊W são fixos, como os valores de condutância dos memristores.
O script mostra como aplicar uma entrada vetorial 𝑋
X a uma rede neural com uma camada oculta."""

import numpy as np

# --- Funções auxiliares ---
def relu(x):
    return np.maximum(0, x)

# --- Entradas (vetor simulado de uma imagem ou sensor) ---
X = np.array([1.0, 0.5, -1.5, 2.0])  # entrada de 4 elementos (pode vir do DAC)

# --- Pesos simulando condutâncias de memristores ---
# Pesos da camada de entrada para camada oculta (4 entradas x 3 neurônios)
W1 = np.array([
    [0.8, -0.5, 0.3],
    [0.2,  0.7, 0.1],
    [-0.3, 0.9, -0.4],
    [0.5, 0.1, -0.6]
])

# Bias da camada oculta
b1 = np.array([0.1, -0.2, 0.05])

# Pesos da camada oculta para camada de saída (3 x 2)
W2 = np.array([
    [0.6, -0.1],
    [-0.3, 0.8],
    [0.4, 0.2]
])

# Bias da saída
b2 = np.array([0.0, 0.1])

# --- Inferência (simulação do hardware) ---
# Etapa 1: produto matriz-vetor com W1
Z1 = np.dot(X, W1) + b1
A1 = relu(Z1)  # simula ativação ReLU no FPGA/ARM

# Etapa 2: produto matriz-vetor com W2
Z2 = np.dot(A1, W2) + b2
Y = relu(Z2)  # saída final da rede

# --- Resultados ---
print("Entrada X:", X)
print("Ativação camada oculta:", A1)
print("Saída Y:", Y)
