#Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor) / 2.

#Declaração de Variáveis 
area : float
diagMaior : float
diagMenor : float

#Entrada de Dados
diagMaior = float(input('Digite a maior diagonal do losango: '))
diagMenor = float(input('Digite a menor diagonal do losango: '))

#Processamento de Dados
area = (diagMaior * diagMenor) / 2

#Saída de Dados
print(f'A área do losango é {area}')