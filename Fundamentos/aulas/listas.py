# Listas:
lista1 = [1, 2, 3, 4]
lista2 = [4, 3, 2, 1]
lista_homogenia = [2, 'a', 5.44, True, None]
lista_dentro_lista = ['um', 'dois', 'três', [1, 2, 3]]

print(lista1[0])
print(lista2[3])
print(lista1[-1])
print(lista_homogenia[1:3])
print(lista_dentro_lista[:])

print('-' * 50)

# Encontre a maior idade entre as idades da lista
idades = [27, 49, 12, 70, 84, 35, 27, 77, 94]

'''SOLUÇÃO 1'''
maior_idade = idades[0]

for idade in idades:
    if idade > maior_idade:
        maior_idade = idade

print(f'Maior idade: {maior_idade}')

'''SOLUÇÃO 2'''
print(f'Maior idade: {max(idades)}')

print('-' * 50)

lista = [2, 'a', 'b', 'c', 5.44, True]
lista.append(999)  # Adiciona valores ao final da lista
lista.append(None)
lista.append(21 / 2)
lista.append(2 == 5 / 2)  # Adiciona um False ao final da lista
lista.append(True)
print(lista)

lista[3] = 'a'  # Substitui um valor no índice 3
lista[-1] = 999  # Substitui um valor no último índice

print(lista)

lista.remove('a')  # Remove a primeira ocorrência de 'a'
print(lista)

print('-' * 50)

l1 = [30, 10, 20]
l2 = [2, 'a', 5.44, True]

print(l1 + l2)  # Concatenação
print(l1 * 3)  # Repetição
print(l1 in l2)  # Filiação

print(len(l2))
print(sum(l1))
print(max(l1))

l2.reverse()  # Inverte a ordem dos elementos
print(l2)
l1.extend([10, 20, 30, 40, 10])  # Adiciona elementos de outra sequência
print(l1)
l1.sort()  # Ordena os elementos
print(l1)
l2.insert(2, 'Novo valor')  # insere um novo elemento no índice desejado
print(l2)
l2.pop()  # Remove o último elemento
print(l2)
l2.clear()  # Remove todos os elementos
print(l2)

print(l1.index(40))  # retorna o índice da primeira ocorrência do elemento
print(l1.count(10))  # conta as ocorrências do elemento
