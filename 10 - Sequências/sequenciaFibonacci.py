"""
Funções: Laço simples - Gerar os n primeiros termos de Fibonacci

Construa um algoritmo que pegue um número inteiro n e gere os n primeiros termos da sequência de Fibonacci. 
Lembrando que a sequência de Fibonacci é definida da seguinte forma:
F_{1} = 1
f_{2} = 1
f_{i} = f_{i-1} + f_{i-2} para i >= 3
ex. se n = 8, seu algoritmo deve imprimir a sequência 1, 1, 2, 3, 5, 8, 13, 21.
"""

def fib(n):
    cont = 1
    penultimo = 1
    ultimo = 1
    f = [1,1]
    if n == 1:
        print(ultimo)
    elif n == 2:
        print(ultimo, penultimo)
    else:
        for cont in range(2,n):
            proximo = f[cont-1] + f[cont-2]
            f.append(proximo)
        print(f)
n = int(input())
fib(n)
