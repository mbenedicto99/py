import random
import matplotlib.pyplot as plt

from random import (randrange, seed)

#randon-fixo
random.seed(12)

#cria lista vazia
notas_matematica = []

#loop de 8
for notas in range(8):
    #apend de numeros randomicos entre 0 e 10
    notas_matematica.append(randrange(0,11))

#lista entre 1 e 8
x = list(range(1, 9))
#captura lista de numero randomicos
y = notas_matematica

#plota eixos x e y com marcador"o"
plt.plot(x, y, marker='o')
#titulo
plt.title('Notas Matematica')
plt.xlabel('PROVAS')
plt.ylabel('NOTAS')
plt.show()
