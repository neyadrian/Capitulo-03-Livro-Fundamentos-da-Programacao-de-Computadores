#Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
    #a) A idade dessa pessoa em anos
    #b) A idade dessa pessoa em meses
    #c) A idade dessa pessoa em dias
    #d) A idade dessa pessoa em semanas

#Declaração de Variáveis
anoNasc : int 
anoAt : int 
idEmAnos : int 
idEmMeses : int 
idEmDias : int
idEmSem : int 

#Entrada de Dados
anoNasc = int(input('Informe seu ano de nascimento: '))
anoAt = int(input('Infomer o ano em que você está: '))

#Processamento de Dados 
idEmAnos = anoAt - anoNasc
idEmMeses = idEmAnos * 12
idEmDias = idEmAnos * 365
idEmSem = idEmMeses * 4

#Saída de Dados
print(f'Sua idade em ANOS é {idEmAnos}')
print(f'Sua idade em MESES é {idEmMeses}')
print(f'Sua idade em DIAS é {idEmDias}')
print(f'Sua idade em SEMANAS é {idEmSem}')

