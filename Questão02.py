#Faça um programa que receba três números, calcule e faça a multiplicação desses números.

#Declaração de Variáveis
num1 : int
num2 : int
num3 : int
mult : int

#Entrada de Dados 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Processamento de Dados
mult = num1 * num2 * num3

#Saída de Dados
print(f'O resultado da sua multiplicação foi: {mult}.')