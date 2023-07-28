# Estrutura de repetição while:
"""
while <expressão>:
    <bloco de código a ser repetido enquanto a expressão for verdadeira>
"""

n = 15
soma = 0
contador = 0
while contador <= n:
    soma += contador
    contador += 1
print(f'A soma dos primeiros {n} números inteiros é {soma}')

print('-' * 50)

# Estrutura de repetição for ... in:
"""
for <item> in <sequencia>
    <bloco de código a ser repetido para cada item da sequência>
"""
numero = '4589'
soma1 = 0
for c in numero:
    soma1 += int(c)
print(f'O resultado da soma é {soma1}')

p = 'araraquara'
count_a = 0
count_r = 0
for letra in p:
    if letra == 'a':
        count_a += 1
    if letra == 'r':
        count_r += 1
print(f"A palavra {p} possui {count_a} letras 'a' e {count_r} letras 'r'")

print('-' * 50)

# Função range:
# range(inicio, fim, incremento)
'''
range(6) -> 0, 1, 2, 3, 4, 5
range(3, 8) -> 3, 4, 5, 6, 7
range(0, 21, 5) -> 0, 5, 10, 15, 20
range(2, 10, 2) -> 2, 10, 2
'''
x = 15
soma2 = 0
for num in range(x + 1):
    soma2 += num
print(f'A soma dos primeiros {x} inteiros é {soma2}')

print('-' * 50)

# BREAK:
"""
for <item> in <sequencia>
    <bloco de código a ser repetido para cada item da sequência>
    if <expressão>:
        <outro bloco de código>
        break
"""
for num in range(250, 301):
    # verifica se o número é divisível por 21
    if num % 21 == 0:
        print(f'Número encontrado: {num}')
        # se for divisível por 21, interrompe a busca
        break
