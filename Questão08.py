#Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.

#Declaração de Variáveis
peso : float
pesoGramas : float

#Entrada de Dados
peso = float(input('Digite o seu peso: '))

#Processamento de Dados
pesoGramas = peso * 1000

#Saída de Dados
print(f'O seu peso em gramas é {pesoGramas}')