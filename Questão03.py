#Faça um programa que receba dois números, calcule e mostre a divisão do primeiro pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.

#Declaração de Variáveis
num1 : int
num2 : int
div : float

#Entrada de Dados 
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número (Diferente de 0): '))

#Processamento de Dados
div = num1 / num2

#Saída de Dados
print(f'O resultado da sua divisão foi: {div}.')