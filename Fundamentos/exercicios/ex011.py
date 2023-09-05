"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma áre a de 2m²
"""
largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

area = largura * altura
litros = area / 2

print(f'A área é {area}m² e a qntd de litros é de {litros}L')
