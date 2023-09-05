"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

angulo = int(input('Digite um ângulo em graus: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'SENO: {seno:.2f}')
print(f'COSSENO: {cosseno:.2f}')
print(f'TANGENTE: {tangente:.2f}')
