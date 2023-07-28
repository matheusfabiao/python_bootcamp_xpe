# Tipos de Operadores
"""
Aritméticos
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
% (módulo ou resto da divisão)
// (divisão inteira)
** (exponenciação)
"""

"""
Comparativos
> (maior que)
>= (maior ou igual que)
< (menor que)
<= (menor ou igual que)
== (igual)
!= (diferente)
"""

"""
Lógicos
and (conjunção)
or (disjunção)
not (complemento)
"""

x = 10
y = 4
z = 4.5
print('x + y + z = ', x + y + z)
print('x - 3 = ', x - 3)
print('x * z = ', x * z)
print('x * 2 = ', x * 2)
print('x / (y + 2) = ', x / (y + 2))
print('x % y = ', x % y)
print('x // y = ', x // y)
print('x ** z = ', x ** z)

print('-'*50)

# calcular a area do trapezio
"""
Formula: area = (B + b) * h / 2
exemplo dado: B = 15, b = 10, h = 8
"""
B = 15
b = 10
h = 8
area = (B + b) * h / 2
print(area)

print('-'*50)

print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 == 10)
print('dez' == 'cinco')
print('dez' != 'cinco')
print('dez' == 'dez')
print(10 != 5)

print('-'*50)

# verifica se uma pessoa pode dirigir (+18 anos E possuir CNH)
idade1 = 18
possui_cnh = True
print(idade1 > 18 and possui_cnh)  # False

# verifica se um passageiro pode viajar sozinho (+18 anos OU possuir autorização)
idade2 = 35
possui_autorizacao = False
print(idade2 > 18 or possui_autorizacao)  # True

# inverter operadores lógicos (not)
print(not True)  # False
print(not False)  # True

print('-'*50)
