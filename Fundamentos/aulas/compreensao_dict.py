# dict comprehension sem condicional
# {chave: valor for item in sequencia}

# dict comprehension com condicional
# {chave: valor for item in sequencia if condicao}

# Todos os números elevados à potência 2
dict_todos = {}
for item in range(1, 11):
    dict_todos[item] = item ** 2
print('Todos os números:', dict_todos)

# Podemos reescrever a mesma operação de outra forma, utilizando dict comprehension
dict_todos1 = {item: item ** 2 for item in range(1, 11)}
print('Todos os números:', dict_todos1)

# Apenas números ímpares elevados à potência 2
dict_impares = {}
for item in range(1, 11):
    if item % 2 != 0:
        dict_impares[item] = item ** 2
print('Números ímpares:', dict_impares)

# Também podemos reescrever utilizando dict comprehension com verificação condicional
dict_impares1 = {item: item ** 2 for item in range(1, 11) if item % 2 != 0}
