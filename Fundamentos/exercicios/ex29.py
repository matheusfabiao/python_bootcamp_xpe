"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input('Velovidade do veículo: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Veículo não será multado.')
else:
    print(f'O veículo foi multado em R${multa:,.2f} por atingir {velocidade} Km/h.')
