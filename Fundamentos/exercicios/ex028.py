"""
Escreva um programa que faça o computador "pensar" em número inteiro
entre 0 e 5 e peça ao usuáio tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

print('-'*50)
print('Vou pensar em um número de 0 a 5. Tente adivinhar')
print('-'*50)

sleep(3)

pc = randint(0, 5)
print('Pronto! Qual o número que pensei?')
print('-'*50)

sleep(3)

user = int(input('Digite sua resposta: '))
print('-'*50)

print('Processando...')

sleep(3)

if 5 >= user >= 0:  # if user <= 5 and user >= 0:
    if pc == user:
        print('-'*50)
        print(f'Parabéns! Pensamos no número {pc}')
        print('-'*50)
    else:
        print('-'*50)
        print(f'Que pena! Pensei no número {pc} e você no {user}')
        print('-'*50)
else:
    print('-'*50)
    print('Erro: Número fora do alcance!')
    print('-'*50)
