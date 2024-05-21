#Faça um programa que receba a temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180 * (C + 32)/100

#Declaração de Variáveis 
tempC : float
tempF : float

#Entrada de Dados
tempC = float(input('Digite a temperatura em Celsius: '))

#Processamento de Dados
tempF = tempC * (9 / 5) + 32

#Saída de Dados
print(f'A temperatura em Fahrenheit é {tempF:.1f}°F')