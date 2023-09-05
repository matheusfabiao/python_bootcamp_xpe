# Conjuntos (set)
c_homog = {3, 0, 4, 3}  # Conjunto homogênio
print(c_homog)  # ordenado e sem elementos repetidos

c_het = {2, 'a', 5.44, True, None, None, True, 'a'}  # Conjunto heterogênio
print(c_het)

# Operações com conjuntos
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# UNIÃO:
print(f'A∪B = {a | b}')
print(f'A∪B = {a.union(b)}')
print('-' * 50)

# INTERSEÇÃO:
print(f'A∩B = {a & b}')
print(f'AuB = {a.intersection(b)}')
print('-' * 50)

# Diferença:
print(f'A-B = {a - b}')
print(f'A-B = {a.difference(b)}')
print(f'A-B = {b.difference(a)}')
print(len(a - b))
print('-' * 50)

# Funções com sets
c1 = {1, 2, 3, 4, 5}
c2 = {4, 5}
c3 = {91, 92, 93}

c1.add(6)  # Adiciona um elemento ao conjunto
print(c1)
print('-' * 50)

c1.update([2, 4, 6, 8])  # Adiciona os elementos de uma sequência iterável
print(c1)  # adicionado apenas o 8, pois os outros elementos eram repetidos
print('-' * 50)

c1.remove(5)  # Remove um elemento do conjunto
print(c1)
print('-' * 50)

c1.discard(8)  # Descarta (remove) um elemento do conjunto
print(c1)
c1.discard(99)  # Diferente do remove(), ele não gera um erro se o elemento a ser removido não existir
print(c1)
print('-' * 50)

print(c1.isdisjoint(c2))  # Verifica se são disjuntos (não possuem elementos em comum)
print(c1.isdisjoint(c3))
print('-' * 50)

print(c1.issubset(c2))  # Verifica se o conjunto é subconjunto de outro
print(c2.issubset(c1))
print('-' * 50)

print(c1.issuperset(c2))  # Verifica se o conjunto contém outro conjunto (superset)
print(c2.issuperset(c1))
print('-' * 50)

"""
Exemplo prático:
Considere que estamos desenvolvendo um programa para gerenciar uma escola de línguas
estrangeiras que possui três turmas de alunos para os seguintes idiomas: Inglês, Espanhol e Frânces.
Considere também, que um mesmo aluno pode estar matriculado em uma única turma ou em múltiplas turmas.
1. Crie uma relação com todos os alunos da escola, sem repetições;
2. Identifique os alunos que estão matriculados em pelo menos duas turmas;
"""
ingles = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}
espanhol = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}
frances = {'Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina'}

uniao = ingles | espanhol | frances
inters = (ingles & espanhol) | (ingles & frances) | (espanhol & frances)  # União das interseções

print(f'Todos os alunos: {uniao}')
print(f'Alunos em pelo menos 2 turmas: {inters}')
