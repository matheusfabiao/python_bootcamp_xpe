# Sintaxe das funções:
"""
def nome_da_funcao(argumento1, argumento2, ...):
    <bloco de código a ser executado>
    return resultado
"""
l1 = [1, 2, 3, 4, 5]
l2 = [3, 1, 5, 9, 0, 8, 2, 3, 4]
l3 = [12, 43, 23, 12, 789]

# itera sobre cada lista e soma seus elementos
'''
MÉTODO SEM FUNÇÕES:

soma_l1 = 0
for item in l1:
    soma_l1 += item
    
soma_l2 = 0
for item in l2:
    soma_l2 += item
    
soma_l3 = 0
for item in l3:
    soma_l3 += item
    
print(f'Resultado: l1 = {soma_l1}, l2 = {soma_l2}, l3 = {soma_l3}')
'''

# MÉTODO COM FUNÇÕES:
def soma_lista(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma


soma_l1 = soma_lista(l1)
soma_l2 = soma_lista(l2)
soma_l3 = soma_lista(l3)

print(f'Resultado: l1 = {soma_l1}, l2 = {soma_l2}, l3 = {soma_l3}')


def multiplica_lista(lista):
    resultado = 1
    for item in lista:
        resultado = resultado * item
    return resultado


soma_l1 = multiplica_lista(l1)
soma_l2 = multiplica_lista(l2)
soma_l3 = multiplica_lista(l3)

print(f'Resultado: l1 = {soma_l1}, l2 = {soma_l2}, l3 = {soma_l3}')

print(multiplica_lista([1, 2, 3, 4, 5]))  # É possível passar uma lista não declarada antes direto nos arg de entrada
