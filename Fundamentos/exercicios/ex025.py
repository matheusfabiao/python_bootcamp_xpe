"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
"""
nome = str(input('Digite seu nome completo: ')).title().strip()
nomes = nome.split(' ')  # Cria uma lista com os nomes digitados, separados por espaço
if "Silva" in nomes:
    print(f'Você tem Silva no nome, {nomes[0]}.')
else:
    print(f'Você não tem Silva no nome, {nomes[0]}.')
