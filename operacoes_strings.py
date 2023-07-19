# Uma String é formada por uma sequência de caracteres
palavra = 'consolação'

# índices positivos
print('Primeiro caractere: ', palavra[0])
print('Segundo caractere: ', palavra[1])
print('Sexto caractere: ', palavra[5])
print('Último caractere: ', palavra[9])

print('-'*50)

# índices negativos
print('Último caractere: ', palavra[-1])
print('Penúltimo caractere: ', palavra[-2])
print('Antepenúltimo caractere: ', palavra[-3])
print('Primeiro caractere: ', palavra[-10])

print('-'*50)

#subpalavras -> slicing ou fatiamento
print(palavra[3:6])  # fatiar do índice 3 até o índice 5
print(palavra[6:10])  # fatiar do índice 6 até o índice 9
print(palavra[2:8])  # fatiar do índice 2 até o índice 7
print(palavra[:7])  # fatiar do início até o índice 6
print(palavra[:7])  # fatiar do índice 2 até o índice 7
print(palavra[6:])  # fatiar do índice 6 até o final
print(palavra[:])  # fatiar do início ao fim (palavra inteira)

print('-'*50)

# Operadores de Strings
print('Matheus' + 'Fabiao')  # concatenação
print('ar' * 2)  # repetição (mesmo de 'ar' + 'ar')

s1 = 'consolação'
s2 = 'sola'
print(s1 in s2)
print(s2 in s1)
print('sola' in s1)
print('solar' in s1)
print('solar' not in s1)
print('solar' not in s2)

print('-'*50)

# Funções e Métodos das Strings
print(len(palavra))  # Consolação = 10 caracteres

a = 'João Pessoa'
b = 'Esta é uma frase, com vírgula.'
c = '     palavra com espaços     '

print(a.upper())  # todas as letras maiúsculas
print(a.lower())  # todas as letras minúsculas
print(b.title())  # primeira letra das palavras em maiúsculo
print(a.replace('João', 'Maria'))  # substitui uma palavra por outra
print(a.startswith('João'))  # verifica se a string começa com...
print(a.endswith('Pessoas'))  # verifica se a string termina com...
print(b.find('frase'))  # retorna o índice da primeira ocorrência da palavra
print(b.split())  # particiona a string em outras, que são separadas por um espaço
print(b.split(','))  # particiona a string em outras, que são separadas por ','
print(c.strip())  # remove os espaços extras no início e no fim da string
