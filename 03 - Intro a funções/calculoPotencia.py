"""
Funções: Laço simples - Cálculo de potência de inteiros via função
Fazer uma função implementando obrigatoriamente a função de nome potencia(x,n) que receba um número inteiro x e um 
número natural n maior ou igual a 0 e que devolva a potência n de x. Fazer um programa principal que solicite do usuário o 
inteiro x e o natural n (nesta ordem!) e usando obrigatoriamente a função, imprima o valor de n de x.

Observacão 1: o cômputo da potência em potencia(x,n) deve ser feito obrigatoriamente usando apenas soma e produto, ou seja, 
NÃO pode usar x**n. A verificação de aderência a estas restricões será posterior ao fechamento das submissões!

Observação 2: Por definição, todo número não nulo elevado a 0 resulta 1, dessa forma, para todo x != 0 => x0 = 1, mas 0n=0 (n>0).
"""
def potencia(x,n):
    i = 0
    pot = 1
    while i < n:
        pot = pot * x
        i += 1
    return pot
x = int(input())
n = input()
potencia(x,n)
print(potencia(x,n))