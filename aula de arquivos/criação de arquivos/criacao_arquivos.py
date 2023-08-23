# Criação de arquivos -> open(caminho, modo)
"""
r - modo de leitura
w - modo de escrita que cria ou substitui um arquivo (caso ele já exista)
x - modo de escrita que cria um arquivo e retorna um erro caso ele já exista
a - modo de escrita que cria um arquivo, caso ele não exista, e adiciona novos dados apenas ao final (como um método append)
t - abre o arquivo no modo texto
b - abre o arquivo no modo binário
"""
arquivo = open('arquivo_somente_leitura.txt', 'r')
# realizaria as operações de leitura
arquivo.close()

arquivo1 = open('valores.txt', 'w')
# realizaria as operações de leitura
arquivo1.close()

arquivo2 = open('valores_dois.txt', 'x')
# realizaria as operações de leitura
arquivo2.close()
