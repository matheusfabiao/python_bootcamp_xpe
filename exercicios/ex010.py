"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
OBS: Considere o Dólar a 4,80 (ago - 2023)
"""
valor = float(input('Digite o valor em reais: '))
print(f'Valor de R${valor:.2f} convertido em Dólares: US${valor / 4.8:.2f}')
