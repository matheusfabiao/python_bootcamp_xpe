# Sintaxe:
# valor_se_verdadeiro if condicao else valor_se_falso

# Método tradicional
nome = 'Matheus'
if len(nome) > 5:
    var = 100
else:
    var = 0
print('O valor de var é:', var)

# Método com atribuição condicional
nome1 = 'Matheus'
var1 = 100 if len(nome1) > 5 else 0
print('O valor de var é:', var1)
