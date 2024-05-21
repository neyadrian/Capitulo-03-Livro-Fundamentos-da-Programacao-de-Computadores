#Faça um programa que receba o peso de uma pessoa, calcule e mostre:
    #a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
    #b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

#Declaração de Variáveis
peso : float
pesoEng : float
pesoEm : float
p1 : float
p2 : float

#Entrada de Dados
peso = float(input('Digite o seu peso: '))

#Processamento de Dados
pesoEng = peso * 15/100
p1 = pesoEng + peso
pesoEm = peso * 20/100
p2 = peso - pesoEm

#Saída de Dados
print(f'Se engordar 15% do seu peso, o novo peso será: {p1}Kg.')
print(f'Se emagrecer 20% do seu peso, o novo peso será: {p2}Kg.')