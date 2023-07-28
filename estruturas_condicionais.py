# Estrutura condicional IF:
'''
if <expressão>
    <bloco de código se a expressão é verdadeira>
'''

y = 0
a = 0
b = 0
c = 0
x = 50
if x > 10:
    y = x + 99
    a = x * 2
    b = x + 2
    c = x ** 2
print(y, a, b, c)

print('-' * 50)

idade = 18
if idade >= 18:
    print('Idade suficiente para a CNH!')

tempo_contribuicao = 35
if idade >= 65 or tempo_contribuicao >= 35:
    print('Habilitado para solicitar a aposentadoria!')

if idade < 65 and tempo_contribuicao < 35:
    print('Não habilitado para solicitar a aposentadoria!')

print('-' * 50)

# Estrutura condicional IF - ELSE:
'''
if <expressão>
    <bloco de código se a expressão é verdadeira>
else:
    <bloco de código se a expressão é falsa>
'''
var1 = 5
var2 = 0
if var1 > 10:
    print(f'O valor de {x} > 10')
    var2 = var1 * 2
else:
    print(f'O valor de {x} <= 10')
    var2 = var1 ** 2
print(var2)

if idade >= 65 or tempo_contribuicao >= 35:
    print('Habilitado para solicitar a aposentadoria!')
else:
    print('Não habilitado para solicitar a aposentadoria!')

print('-' * 50)

# Estrutura condicional IF - ELIF - ELSE:
'''
if <expressão 1>:
    <bloco de código se a expressão 1 é verdadeira>
elif <expressão 2>:
    <bloco de código se a expressão 2 é verdadeira>
else:
    <bloco de código se nenhuma expressão for verdadeira>
'''

idade_pessoa = 22  # variável de idade da pessoa
'''
EXEMPLO DE CÓDIGO MAL ESCRITO:
if idade_pessoa < 12:
    faixa_etaria = 'crianca'
else:
    if idade < 18:
        faixa_etaria = 'adolescente'
    else:
        if idade < 60:
            faixa_etaria = 'adulto'
        else:
            faixa_etaria = 'idoso'
'''

# Código bem esrito:
if idade_pessoa < 12:
    faixa_etaria = 'crianca'
elif idade_pessoa < 18:
    faixa_etaria = 'adolescente'
elif idade_pessoa < 60:
    faixa_etaria = 'adulto'
else:
    faixa_etaria = 'idoso'
print(f'Faixa Etária: {faixa_etaria}')
