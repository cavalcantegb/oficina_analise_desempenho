# Aluno: Guilherme Bastos Cavalcante
# Matricula: 382072
import numpy as np
from numpy import random
from matplotlib import pyplot as plt

# Questao1
print('Questao 1:\n')

## item a
tamanho_vetor = random.randint(100,501)
print('item a')
print('\t Tamanho do vetor: ', tamanho_vetor)

## item b e c
vetor = random.randint(low=1, high=501, size = tamanho_vetor)
idade = 27
print('item b e c: ')
print('\t Vetor x Idade: \n\t', vetor * idade)

# Questao 2
print('\nQuestao 2')

## item a
tamanho = vetor.size
media = vetor.mean()
mediana = np.median(vetor)
variancia = np.var(vetor)

print('item a')
print('\tTamanho do vetor = %d' % tamanho)
print('\tMedia vetor = {0}'.format(media))
print('\tMediana = {}\n\tVariancia = {}'.format(mediana, variancia))

## item b
## Caso o tkinter nao esteja instalado
### `sudo apt-get install python3-tk`
plt.hist(vetor)
plt.show()