#Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade salários mínimos que esse funcionário ganha.

#Declaração de Variáveis
salMin : float
salFun : float
result : float

#Entrada de Dados
salMin = float(input('Digite o valor do salário mínimo: '))
salFun = float(input('Digite o valor do salário do funcionário: '))

#Processamento de Dados
result = salFun / salMin

#Saída de Dados 
print(f'Quantidade de salários mínimos {result}')