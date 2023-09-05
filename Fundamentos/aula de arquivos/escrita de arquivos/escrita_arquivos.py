# Escrita de uma linha no arquivo
arquivo = open('cidades.txt', 'a')
arquivo.write('\nRJ; São Gonçalo; 1031903')
arquivo.close()

# Adicionando uma lista de valores para o arquivo
linhas = [
    '\nDP; Brasília; 2852372\n',
    'CE; Fortaleza: 2571896\n',
    'MG; Belo Horizonte; 2491109\n',
]
arquivo = open('cidades.txt', 'a')
arquivo.writelines(linhas)
arquivo.close()
