#Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado

#Declaração de Variáveis
area : float
lado1 : float
lado2 : float

#Entrada de Dados
lado1 = float(input('Digite o lado do quadrado: '))
lado2 = float(input('Digite o outro lado do quadrado: '))

#Processamento de Dados
area = lado1 * lado2

#Saída de Dados
print(f'A área do quadrado é {area}')