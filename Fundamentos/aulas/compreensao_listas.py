# list comprehension sem condicional
# [expr(item) for item in sequencia]

# list comprehension com condicional
# [expr(item) for item in sequencia if condicao]

# Criar uma lista com os números de 1 a 10 elevados à 2
potencias = []
for item in range(1, 11):
    potencias.append(item ** 2)
print(potencias)

# Podemos reescrever a mesma operação de outra forma, utilizando list comprehension
potencias1 = [{item ** 2} for item in range(1, 11)]
print(potencias1)

# Multiplica por 10 os números de 1 a 15
l1 = [n * 10 for n in range(1, 16)]
print(l1)

# Cria lista com os caracteres em maiúsculo
l2 = [c.upper() for c in 'Matheus']
print(l2)

# Indica se n é par ou não
l3 = [(n % 2 == 0) for n in range(0, 10)]
print(l3)

# Cria uma lista com os números ímpares de 1 a 10 elevados à 2
potencias2 = []
for item in range(1, 11):
    if item % 2 != 0:
        potencias2.append(item ** 2)
print(potencias2)

# Também podemos reescrever utilizando list comprehension com verificação condicional
potencias3 = [item ** 2 for item in range(1, 11) if item % 2 != 0]
print(potencias3)
