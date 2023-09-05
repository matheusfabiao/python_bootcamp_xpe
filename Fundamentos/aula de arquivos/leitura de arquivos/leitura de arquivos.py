# Lê o conteúdo inteiro e armazena numa variável (não recomendado)
arquivo = open('cidades.txt', 'r')
linhas = arquivo.read()
arquivo.close()
print(linhas)
print(type(linhas))

print('-'*50)

# Lê o conteúdo inteiro e armazena linha por linha em uma lista de Strings
arquivo = open('cidades.txt', 'r')
linhas1 = arquivo.readlines()
arquivo.close()
print(linhas1)
print(type(linhas1))
print('Qntd de linhas do arquivo:', len(linhas1))

print('-'*50)

# Remoção do "\n" na lista "linhas1"
novas_linhas = []  # criação de uma nova lista
for linha in linhas1:
    novas_linhas.append(linha.rstrip())  # remove espaços em branco e os \n
print(novas_linhas)

print('-'*50)

# É possível iterar sobre o arquivo diretamente
arquivo = open('cidades.txt', 'r')
for linha in arquivo:
    print(linha.rstrip())
arquivo.close()

print('-'*50)

# Soma do número de habitantes de cada cidade
arquivo = open('cidades.txt', 'r')
soma = 0
for linha in arquivo:
    cidade = linha.split(' ')
    populacao = int(cidade[-1])
    print(populacao)
    soma += populacao
arquivo.close()
print('Soma dos habitantes:', soma)
