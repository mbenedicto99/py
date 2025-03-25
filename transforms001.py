import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# 1. Carregar e preparar a imagem
# ResNet18, que é uma rede neural convolucional treinada no ImageNet (com 1000 classes).
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),  # converte para tensor PyTorch
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # valores padrão para modelos pré-treinados
                         std=[0.229, 0.224, 0.225])
])

img_path = 'caminho/para/sua_imagem.jpg'  # substitua pelo caminho da imagem usada no desenho
image = Image.open(img_path).convert('RGB')
input_tensor = transform(image).unsqueeze(0)  # adiciona dimensão batch

# 2. Carregar modelo pré-treinado
model = models.resnet18(pretrained=True)
model.eval()  # modo de inferência

# 3. Fazer a inferência
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, 1).item()

# 4. Interpretar o resultado
# Baixar os nomes das classes do ImageNet
import json
import urllib.request

url = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
classes = urllib.request.urlopen(url).read().decode('utf-8').splitlines()

print(f"Classe prevista: {classes[prediction]}")
