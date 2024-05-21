#Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber, de acordo com as regras a seguir: 
    #a) a hora trabalhada vale 1/8 do salário mínimo; 
    #b) a hora extra vale 1/4 do salário mínimo; 
    #c) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada; 
    #d) a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra; 
    #e) o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras.

#Declaração de Variáveis
hTrab : float
salMin : float 
hETrab : float
vHT : float 
vHET : float
salBruto : float 
hExtraARec : float 
sFinal : float 

#Entrada de Dados
hTrab = float(input("Digite o total de horas trabalhadas: "))
salMin = float(input("Digite o valor do salário mínimo: "))
hETrab = float(input("Digite o total de horas extras trabalhadas: "))

#Processamento de Dados
vHT = salMin / 8
vHET = salMin / 4
salBruto = hTrab * vHT
hExtraARec = hETrab * vHET
sFinal = salBruto + hExtraARec

#Saída de Dados
print(f"O valor do salário a receber é de R$ {sFinal}")