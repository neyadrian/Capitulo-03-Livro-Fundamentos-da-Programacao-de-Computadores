#Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180 graus.

#Declaração de Variáveis
ang1 : float
ang2 : float
result : float

#Entrada de Dados
ang1 = float(input("Digite o valor do primeiro ângulo: "))
ang2 = float(input("Digite o valor do segundo ângulo: "))

#Processamento de Dados
result = 180 - (ang1 + ang2)

#Saída de Dados
print(f"O valor do terceiro ângulo é de {result}°")