# Exibe msg de boas vindas ao usuário
def boas_vindas(nome):
    print(f'Olá {nome}! Seja bem-vindo(a)!')


# Calcula a área de um quadrado: lado x lado
def area_quadrado(lado):
    return lado * lado


# Calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura):
    return (base * altura) / 2


# Realiza as chamadas das funções
boas_vindas('Matheus')
print(area_quadrado(5))
print(area_triangulo(4, 5))


def funcao_sem_retorno(a, b):
    soma = a + b
    # return soma


print(funcao_sem_retorno(2, 6))


# Realiza uma divisão. Se o divisor é zero, retorna uma msg de erro.
def div(dividendo, divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return  # Semelhante ao Break, interrompe a execução da função
    return dividendo / divisor


# Função similar à função div(), mas que retorna o dividendo e o resto da divisão
def div_qr(dividendo, divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return  # Semelhante ao Break, interrompe a execução da função
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto


print('div(10, 4) =', div(10, 4))
print('div_qr(10, 4) =', div_qr(10, 4))
print('div(10, 0) =', div(10, 0))

# Atribuição dos múltiplos valores em uma variável única do tipo tupla
resultado = div_qr(21, 5)
print('Resultado: ', resultado, type(resultado))

# Atribuição dos múltiplos valores em variáveis separadas
quociente, resto = div_qr(21, 5)
print('Quociente: ', quociente, type(quociente))
print('Resto: ', resto, type(resto))


# Reaproveitando ainda mais o código (Princípio SOLID)
def divisor_invalido(divisor):
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return True
    return False


# Retorna o resultado de uma divisão
def div2(dividendo, divisor):
    if divisor_invalido(divisor):
        return
    return dividendo / divisor


# Retorna o quociente e o resto de uma divisão
def div_qr2(dividendo, divisor):
    if divisor_invalido(divisor):
        return
    quociente2 = dividendo // divisor
    resto2 = dividendo % divisor
    return quociente2, resto2
