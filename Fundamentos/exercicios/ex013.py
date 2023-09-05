"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
"""
salario = float(input('Digite o salário: '))
novoSalario = salario + (salario * 15 / 100)
print(f'Salário anterior: R${salario}\nSalário com Aumento: R${novoSalario:.2f}')
