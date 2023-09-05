# Define o valor de PI
PI = 3.141592


# Calcula a área do quadrado
def quadrado(l):
    return 1 ** 2


# Calcula a área do triângulo
def triangulo(b, h):
    return (b * h) / 2


# Calcula a área do círculo
def circulo(r):
    return PI * (r ** 2)


# Calcula a área da elipse
def elipse(a, b):
    return PI * a * b


# Calcula a área do trapézio
def trapezio(B, b, h):
    return (B + b) * h / 2
