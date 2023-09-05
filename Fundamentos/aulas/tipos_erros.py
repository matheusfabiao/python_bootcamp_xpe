# Erro de Sintaxe:
# São os erros ocasionados pela violação da sintaxe do Python
x = 3
y = 5
# INCORRETO -> print x + y
# CORRETO -> print (x + y)


# Erro de Execução:
# Surgem quando o interpretador não executar uma instrução devido à alguma inconsistência
w = 0
# INCORRETO -> print(ww)
# CORRETO -> print(w)


# Erros Lógicos:
# É o tipo de erro mais difícil de lidar, pois o erro não é de fato detectado
a = 5.0
b = 7.0
c = 12.0
# INCORRETO -> media = a + b + c / 3
# CORRETO -> media = (a + b + c) / 3

"""
OUTROS EXEMPLOS:
1variavel = 0 -> Sintaxe
"""

"""
if num == 3:
print("num é igual à 3") -> Sintaxe (identação)
"""

"""
var1 = 1000
print(var1)
var2 = 0
print(var2)
var3 = a / b
print(var3) -> Erro de Execução
"""

"""
cidade = "João Pessoa"
print(cidade)
estado = "Paraíba"
print(estado)
print(cidade, estado, pais) -> Erro de Execução
"""
