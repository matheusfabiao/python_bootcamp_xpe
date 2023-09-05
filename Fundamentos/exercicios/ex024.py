"""
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santo"
"""
cidade = str(input('Digite o nome da cidade: ')).title().strip()
c = cidade.split(' ')
# if 'Santo' in c[0]:
#     print(f'{cidade} começa com "Santo"')
# else:
#     print(f'{cidade} não começa com "Santo"')

resposta = f'{cidade} começa com "Santo"' if 'Santo' in c[0] else f'{cidade} não começa com "Santo"'
print(resposta)
