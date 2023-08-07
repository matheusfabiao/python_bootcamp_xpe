"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
qntdKm = int(input('Digite a qntd de Km percorridos: '))
qntdDias = int(input('Digite a qntd de dias que o carro foi alugado: '))
preco = (60 * qntdDias) + (0.15 * qntdKm)
print(f'Total a pagar: R${preco:.2f}')
