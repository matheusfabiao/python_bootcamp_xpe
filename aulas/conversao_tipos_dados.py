# Conversão de tipos de dados
# Formula: <tipo a ser convertido>(nome da variavel)
nascimento = 2001
ano_atual = 2023
idade = ano_atual - nascimento
saida = 'Eu tenho ' + str(idade) + ' anos'
print(saida)

print('ano_atual:', type(ano_atual))
print('ano_atual convertido:', type(str(ano_atual)))

print('-'*50)

print(int(float('99.0')))# realiza primeiro a conversão para float e depois para inteiro, caso contrário daria um erro de tempo de execução

print('-'*50)

print(int(True))
print(int(False))
print(float(True))
print(float(False))
print(str(True))
print(str(False))

print('-'*50)

print(str(None))  # None só pode ser convertido para String ou Boolean
print(bool(None))

print('-'*50)

# Formatação com f-strings
variavel = 10
print(f'Exemplo de f-string com um valor {variavel} e uma expressão {variavel + 1}')
print(f'Eu tenho {idade} anos')  # exemplo com a variavel idade la em cima

palavra = 'paralelepípedo'
print(f'A palavra {palavra.upper()} possui {len(palavra)} letras')

orcamento = 5000
vlr_gasto = 430
pct = (vlr_gasto/orcamento) * 100
print(f'Porcentagem já gasta do orçamento: {pct}%')
print(f'Porcentagem já gasta do orçamento: {pct:.2f}%')  # .xf é o controle de casas decimais

pct2 = (vlr_gasto/orcamento)
print(f'Porcentagem já gasta do orçamento: {pct2:.2%}')  # ao substituir o "f" por "%", o python já coloca em forma de porcentagem
