# Dicionários
# chave1:valor1 , chave2:valor2

d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}  # chaves tipo String
print(d1)

d2 = {1: 'um', 2: 'dois', 3: 'três'}  # chaves tipo inteiro
print(d2)

d3 = {2: 'a', 5.44: True, 'key': None}  # chaves e valores mistos
print(d3)

d4 = {}  # Dicionário vazio
print(d4)

d5 = {'um': 1, 'dois': 2, 'três': 3}
# Acesso aos elementos
print(d1['nome'])  # Declara a chave e imprime o valor dessa chave
print(d2[2])  # Declara a chave e imprime o valor dessa chave
print('-'*50)

d1['endereço'] = 'Rua 123'  # Adiciona a chave "endereço" e atribui o valor "Rua 123"
print(d1)
print('-'*50)

print(f'Maior chave: {max(d2)}\nMenor chave: {min(d2)}')  # Maior e menor chave
print('-'*50)

d2.update({4: 'quatro', 5: 'cinco'})
print(d2)
print('-'*50)

print('nome' in d1)  # Verifica se o dict possui as seguintes chaves
print(3 in d2)
print('-'*50)

d2.pop(5)  # Remove o elemento com chave 5
print(d2)
print('-'*50)

# Iteração
for key in d2:  # Ou: for key in d2.values()
    print(key, d2[key])
print('-'*50)

for value in d2.values():
    print(value)
print('-'*50)

for key in d5:  # Ou: for key in d2.keys()
    if key == 'três':
        print('Chave três encontrada')
        break
print('-' * 50)

soma = 0
for value in d5.values():
    soma += value
print('soma dos valores do dicionário:', soma)
print('-'*50)

for key, value in d1.items():
    print(f'Chave: {key} , Valor: {value}')
print('-'*50)

# OBS1: uma tupla pode ser utilizada como chave composta
# OBS2: uma lista já não pode ser utilizada como chave
dic = {}
dic['chave1'] = 99  # Chave de exemplo
dic[(0, 1, 2)] = 'Chave composta'
print(dic)
print(dic[(0, 1, 2)])
