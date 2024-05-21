#Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.

#Declaração de Variáveis
note1 : float
note2 : float
mediaPond : float

#Entrada de Dados 
note1 = float(input('Digite a primeira nota: '))
peso1 = 2

note2 = float(input('Digite a segunda nota: '))
peso2 = 3 

#Processamento de Dados
resultPeso = (peso1 + peso2)
resultNote = (note1 * peso1) + (note2 * peso2)
mediaPond = resultNote / resultPeso

#Saída de Dados]
print(f'O resultado da sua média ponderada é: {mediaPond}.')