# Finalidade  : CNN - Classificação de Imagens de Plataforma
# Autor       : Marcos de Benedicto (AI SUpport)
# Data        : 27032025
# Input       : Dados Estruturais
# Output      : Modelo de Analise

# Esse código espera que você tenha imagens organizadas em duas classes:
# normal/ → plataformas em boas condições
# falha/ → imagens com problemas visíveis

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Diretórios com imagens de treinamento e validação
# Estrutura esperada:
# dataset/
# ├── train/
# │   ├── normal/
# │   └── falha/
# └── val/
#     ├── normal/
#     └── falha/

train_dir = 'dataset/train'
val_dir = 'dataset/val'

# Pré-processamento e aumento de dados
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, zoom_range=0.2,
                                   horizontal_flip=True, fill_mode='nearest')

val_datagen = ImageDataGenerator(rescale=1./255)

# Carregamento dos dados
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Definindo a CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')  # Saída binária: normal ou falha
])

# Compilando o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinamento
history = model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator
)

# Plot da acurácia
plt.plot(history.history['accuracy'], label='Treinamento')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.title('Acurácia do Modelo')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
