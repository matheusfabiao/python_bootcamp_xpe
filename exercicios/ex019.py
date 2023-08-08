"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que o ajude, lendo o nome dos alunos e escrevendo o nome escolhido.
"""

from random import choice

alunos = []
i = 1
while i < 5:
    aluno = str(input(f'Digite o nome do {i}º aluno: '))
    alunos.append(aluno)
    i += 1
print(choice(alunos))
