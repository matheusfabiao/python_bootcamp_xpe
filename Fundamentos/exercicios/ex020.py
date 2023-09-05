"""
O mesmo professor agora quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import choice
alunos = []
i = 1
while i < 5:
    aluno = str(input(f'Digite o nome do {i}º aluno: '))
    alunos.append(aluno)
    i += 1
print(choice(alunos))
