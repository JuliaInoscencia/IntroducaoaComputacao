"""
Laço simples: Dado N, determinar a soma dos N primeiros ímpares
Construa um programa que solicita que o usuário digite um inteiro positivo N e cuja saída seja a soma dos N primeiro ímpares.
"""

n = int(input())
soma = 0
cont = 1
for i in range(n):
    soma+=cont
    cont+= 2
print(soma)