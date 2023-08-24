"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas e minúsculas
2. Quantas letras tem no total (sem contar os espaços)
3. Quantas letras tem o primeiro nome
"""
nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Qntd de Letras: {len(nome) - nome.count(" ")}')
print(f'Qntd de Letras 1º nome: {len(nome1[0])}')
