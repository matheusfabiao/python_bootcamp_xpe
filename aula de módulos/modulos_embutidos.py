# Módulo math: módulo com funções matemáticas p/ cálculos mais complexos
import math
print('Função Cosseno:', math.cos(100))
print('Função Log:', math.log(10))

# Módulo itertools: módulo p/ construção de sequências elaboradas
import itertools
# Combinação de 3 em 3
print('Combinação:', list(itertools.combinations('ABCD', 3)))
# Permutação de 2 em 2
print('Permutação:', list(itertools.permutations('abcd')))

# Módulo datetime: módulo p/ manipulação de timestamps (datas, horas, deltas, etc.)
from datetime import datetime, timedelta
print('Data e hora atual:', datetime.now())
print('Data e hora daqui 7 dias:', datetime.now() + timedelta(days=7))

# Módulo random: módulo p/ criação de números e sequências aleatórias
import random
print('Número aleatório entre 0 e 1:', random.random())
print('Número aleatório entre 50 e 100:', random.randint(50, 100))

# Módulo 'os': módulo p/ funcionalidades que dependem do sistema operacional
import os
# Cria um diretório chamado 'pasta_os'
os.mkdir('pasta_os')
# Caminho completo
nome_pasta = 'pasta_os'
# print(f'\home\matheusfabiao\{nome_pasta}\arquivo.txt')  # ILUSTRATIVO
