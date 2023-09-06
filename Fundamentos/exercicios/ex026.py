"""
Faça um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes aparace a letra "A"
2. Em que posição ela aparece pela primeira vez
3. Em que posição ela aparece pela última vez
"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A primeira letra "A" aparece na posição {frase.find("A") + 1}')
print(f'A última letra "A" aparece na posição {frase.rfind("A") + 1}')
