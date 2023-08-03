"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""
num = int(input('Digite um número: '))
count = 1
while count < 11:
    print(f'{num} * {count} = {num * count}')
    count += 1
