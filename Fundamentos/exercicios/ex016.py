"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
from math import trunc
num = float(input('Digite um número real: '))
print(f'O número {num} tem a parte Inteira {trunc(num)}')

'''
MÉTODO TRADICIONAL:
num_real = float(input('Digite um número real: '))
num_inteiro = int(num_real)
print(f'O número {num_real} tem a parte Inteira {num_inteiro}')
'''
