import numpy as np

# Definir a função ReLU
def relu(x):
    return np.maximum(0, x)

# Definir a função de propagação para a rede neural
def forward_pass(X, weights, biases):
    # Primeira camada
    z1 = np.dot(X, weights['W1']) + biases['b1']
    a1 = relu(z1)

    # Segunda camada
    z2 = np.dot(a1, weights['W2']) + biases['b2']
    a2 = relu(z2)

    # Terceira Camada
    z3 = np.dot(a2, weights['W3']) + biases['b3']
    a3 = relu(z3)

    # Quarta Camada
    z4 = np.dot(a3, weights['W4']) + biases['b4']
    a4 = relu(z4)

    # Camada de saída
    z5 = np.dot(a4, weights['W5']) + biases['b5']
    output = z5  # Sem ativação na saída para este exemplo (regressão)

    return output

# Inicializar os pesos e os bias
def initialize_parameters(input_dim, hidden_dim1, hidden_dim2, hidden_dim3, hidden_dim4, output_dim):
    np.random.seed(42)  # Para reprodução
    weights = {
        'W1': np.random.randn(input_dim, hidden_dim1) * 0.1,
        'W2': np.random.randn(hidden_dim1, hidden_dim2) * 0.1,
        'W3': np.random.randn(hidden_dim2, hidden_dim3) * 0.1,
        'W4': np.random.randn(hidden_dim3, hidden_dim4) * 0.1,
        'W5': np.random.randn(hidden_dim4, output_dim) * 0.1
    }
    biases = {
        'b1': np.zeros((1, hidden_dim1)),
        'b2': np.zeros((1, hidden_dim2)),
        'b3': np.zeros((1, hidden_dim3)),
        'b4': np.zeros((1, hidden_dim4)),
        'b5': np.zeros((1, output_dim))
    }
    return weights, biases

# Gerar dados de entrada
np.random.seed(0)
X = np.random.rand(10, 2)  # 10 exemplos, 2 características

# Configurar a arquitetura da rede
input_dim = 2
hidden_dim1 = 7
hidden_dim2 = 5
hidden_dim3 = 3
hidden_dim4 = 4
output_dim = 1

# Inicializar os parâmetros
weights, biases = initialize_parameters(input_dim, hidden_dim1, hidden_dim2, hidden_dim3, hidden_dim4, output_dim)

# Fazer a propagação direta
output = forward_pass(X, weights, biases)

# Exibir os resultados
print("Entrada:")
print(X)
print("\nSaída da Rede Neural:")
print(output)
