"""
Laço simples: Dado um numero decimal N, determinar a soma de seus dígitos
Construa um programa que solicita que o usuário digite um inteiro positivo N e cuja saída seja a soma dos dígitos do número N digitado. 
Lembre-se que a divisão entre inteiros devolve inteiro e que para pegar o resto deve-se usar o operador binário % 
(ou seja, para a e b variáveis inteiras, se a=19 e b=4, então a divisão inteira de a por b resulta 4 e a%b resulta 3.
"""

n= int(input())
resto = 0
soma = 0
while n > 0:
    resto = n%10
    n = (n-resto)//10
    soma += resto    
print(soma)
