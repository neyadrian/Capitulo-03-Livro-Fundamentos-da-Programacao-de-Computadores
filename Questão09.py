#Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que A = ((base maior + base menor)*altura)/2.

#Declaração de Variáveis
area : float
baseMaior : float
baseMenor : float
altura : float

#Entrada de Dados
baseMaior = float(input('Digite a maior base do trapézio: '))
baseMenor = float(input('Digite a menor base do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

#Processamento de Dados
area = ((baseMaior + baseMenor) * altura) / 2

#Saída de Dados
print(f'A área do trapézio é {area}')