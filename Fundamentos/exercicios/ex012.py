"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input('Digite o preço do produto: '))
novoPreco = preco - (preco * 5 / 100)
print(f'Preço Original: R${preco}\nPreço com Desconto: R${novoPreco:.2f}')
