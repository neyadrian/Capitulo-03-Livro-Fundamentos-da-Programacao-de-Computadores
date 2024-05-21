#João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deverá pagar multa 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de joão.

#Declaração de Variáveis
salario : float
conta1 : float 
conta2 : float 
multa1 : float 
multa2 : float 
result : float 
restoSal : float 

#Entrada de Dados
salario = float(input('Digite o salário de João: '))
conta1 = float(input('Digite o valor da 1ª conta: '))
conta2 = float(input('Digite o valor da 2ª conta: '))

#Processamento de Dados
multa1 = conta1 + 0.2
multa2 = conta2 + 0.2
result = multa1 + multa2
restoSal = salario - result

#Saída de Dados
print(f'O que restou do salário foi {restoSal}')