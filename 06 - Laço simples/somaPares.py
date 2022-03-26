"""
Laço simples: Dado N, determinar a soma dos N primeiros pares
Construa um programa que solicita que o usuário digite um inteiro positivo N, então implemente um laço (obrigatório) que compute a 
soma dos N primeiro pares, imprimindo a soma final. Considere o inteiro 0 como o primeiro número par.
"""

n = int(input())
soma = 0
cont = 0
i = 0 
while i < n:
    soma +=cont
    cont += 2
    i += 1
print(soma)