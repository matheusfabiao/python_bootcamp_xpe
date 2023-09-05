"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
OBS: km - hm - dam - m - dm - cm - mm
"""
valor = float(input('Digite um valor em metros: '))
print(f'Metros: {valor}m\nCentímetros: {valor * 100:.0f}cm\nMilímetros: {valor * 1000:.0f}mm')
