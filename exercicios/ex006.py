"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""
num = int(input('Digite um número: '))
print(f'Número: {num}\nDobro de {num}: {num * 2}\nTriplo: {num * 3}\nRaiz quadrada: {pow(num, (1/2))}')  # pow(num, (1/2)) = num ** (1/2)
