#Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 W de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada. 

#Declaração de Variáveis
largura : float
comprimento : float 
tamanho : float 
potencia : float 

#Entrada de Dados
largura = float(input("Digite a largura do comôdo em metros: "))
comprimento = float(input("Digite o comprimento do comôdo em metros: "))

#Processamento de Dados
tamanho = largura * comprimento
potencia = tamanho / 18

#Saída de Dados
print(f"O tamanho do comôdo é {tamanho:.1f}")
print(f"A potência para iluminação é {potencia:.1f}")