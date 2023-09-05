# Sintaxe:
# lambda argumentos : <expressão>

# Declaração de função explícita (tradicional)
def area_quadrado(lado):
    return lado * lado


# Declaração de função lambda
area_quad = lambda lado: lado * lado
print(area_quad(4))

# Função lambda com mais de um argumento
area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(10, 20))

# Verificação de tipo da variável
print(type(area_quadrado))
print(type(area_quad))
print(type(area_triangulo))

# Função que calcula o triplo do número
triplo = lambda x: x * 3
print(triplo(10))

# Calcula o triplo dos números de uma lista
lista = [4, 5, 9, 7, 0, 1, 8]
print(list(map(triplo, lista)))  # Função map mapeia uma função numa lista

# Podemos reescrever de um jeito mais pythonico ainda!
print(list(map(lambda x: x * 3, [4, 5, 9, 7, 0, 1, 8])))
