#Faça um programa que receba o valor dos catetos de um triângilo, calcule e mostre o valor da hipotenusa.

#Declaração de Variáveis
catOposto : float 
catAdjacente : float 
hipotenusa : float

#Entrada de Dados
catOposto = float(input('Digite o valor do Cateto Oposto: '))
catAdjacente = float(input('Digite o valor do Cateto Adjacente: '))

#Processamento de Dados 
hipotenusa = (catAdjacente ** 2 + catOposto ** 2) ** (1/2)

#Saída de Dados 
print(f'A hipotenusa do Triângulo é {hipotenusa:.1f}')
