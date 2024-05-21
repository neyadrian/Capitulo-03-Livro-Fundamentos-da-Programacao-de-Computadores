#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário de um funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.

#Declaração de Variáveis
sal : float
vendas : float
salFinal : float
comVendas : float

#Entrada de Dados
sal = float(input('Digite o salário do funcionário: '))
vendas = float(input('Digite o valor de vendas do funcionário: '))
porComi = 0.4

#Processamento de Dados
comVendas = vendas * porComi
salFinal = sal + comVendas

#Saída de Dados
print(f'A comissão de vendas do funcionário foi de {comVendas}, e seu salário final foi de {salFinal}')
