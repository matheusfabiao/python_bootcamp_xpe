# Inverter a ordem dos argumentos de entrada sem erro:
# Calula a área de um triângulo
def area_triangulo(base, altura):
    return (base * altura) / 2


print(area_triangulo(5, 10))
print(area_triangulo(altura=10, base=5))


# Argumento padrão (default)
def exibe_pessoa(nome, idade=30):  # A idade por padrão será 30 em todos os casos
    print(f'Meu nome é {nome} e tenho {idade} anos.')


exibe_pessoa('Matheus')  # Não é necessário declarar o segundo argumento
exibe_pessoa('Jorge', 50)  # Argumento de idade antes era 30 (padrão) mas agora é 50
