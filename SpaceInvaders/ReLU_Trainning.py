import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from torch.utils.data import DataLoader, Dataset

# Carregar os dados simulados
data = pd.read_csv("simulated_data.csv")  # Substitua pelo nome do arquivo salvo, se necessário

# Pré-processamento dos dados
le = LabelEncoder()
data['road_condition'] = le.fit_transform(data['road_condition'])  # Codificar labels categóricos

features = ['traffic_volume', 'avg_speed', 'precipitation', 'road_condition', 'hour_of_day']
target = 'accident_occurred'

X = data[features].values
y = data[target].values

# Normalizar os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar um Dataset personalizado
class AccidentDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Criar DataLoaders
train_dataset = AccidentDataset(X_train, y_train)
test_dataset = AccidentDataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Definir o modelo RNN
class RNNModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNNModel, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = x.unsqueeze(1)  # Adicionar dimensão de sequência (batch_size, seq_len=1, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # Estado oculto inicial
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])  # Apenas a saída do último passo de tempo
        return out

# Hiperparâmetros
input_size = len(features)
hidden_size = 16
output_size = 1
learning_rate = 0.001
num_epochs = 20

# Inicializar o modelo, a função de perda e o otimizador
model = RNNModel(input_size, hidden_size, output_size)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Treinamento
def train_model():
    model.train()
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch).squeeze()
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss/len(train_loader):.4f}")

# Avaliação
def evaluate_model():
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            outputs = model(X_batch).squeeze()
            predictions = torch.round(torch.sigmoid(outputs))
            correct += (predictions == y_batch).sum().item()
            total += y_batch.size(0)
    print(f"Accuracy: {correct / total:.4f}")

# Executar treinamento e avaliação
train_model()
evaluate_model()
