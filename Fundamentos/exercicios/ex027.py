"""
Faça um programa que leia  o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza
"""
nome = str(input('Digite seu nome completo: ')).title().strip().split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')
