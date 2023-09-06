"""
Desenvolva um programa que pergunte a distância, em Km, de uma viagem.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
até 200Km e R$0,45 para viagens mais longas.
"""
distancia = float(input('Digite a distância da viagem: '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'A viagem custará {preco}')
