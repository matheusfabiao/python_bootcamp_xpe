"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
"""
from math import hypot
c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjascente = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = hypot(c_oposto, c_adjascente)
print(f'A hipotenusa mede {hipotenusa:.2f}')

"""
OUTRO MÉTODO:
c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjascente = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = (c_oposto ** 2 + c_adjascente ** 2) ** (1/2)
print(f'A hipotenusa mede {hipotenusa:.2f}')
"""
