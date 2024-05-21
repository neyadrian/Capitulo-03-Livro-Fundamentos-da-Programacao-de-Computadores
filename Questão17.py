#Faça um programa que receba o raio, calcule e mostre:
    #a) o comprimento de uma esfera; sabe-se que C = 2 * pi * R;
    #b) a área de uma esfera; sabe-se que A = pi * R²;
    #c) o volume de uma esfera; sabe-se V = 3/4 * pi * R³.

#Declaração de Variáveis
raio : float
pi : float 
comp : float 
area : float 
vol : float

#Entrada de Dados
raio = float(input("Digite o raio: "))
pi = 3.14

#Processamento de Dados
comp = 2 * pi * raio
area = pi * raio ** 2
vol = 3/4 * pi * raio ** 3

#Saída de Dados
print(f"O comprimento é de {comp}")
print(f"A área é de {area}")
print(f"O volume é de {vol}")