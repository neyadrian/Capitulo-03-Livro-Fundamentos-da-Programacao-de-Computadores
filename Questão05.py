#Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

#Declaração de Variáveis 
valor : float
desc : float
novoValor : float

#Entrada de Dados
valor = float(input('Digite o preço do produto: '))

#Processamento de Dados
desc = valor * 0.1
novoValor = valor * 0.9

#Saída de Dados 
print(f'O preço do produto com desconto é de: {novoValor:.2f}.')