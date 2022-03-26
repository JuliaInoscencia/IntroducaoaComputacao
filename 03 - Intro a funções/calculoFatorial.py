"""
Funções: Laço simples - Cálculo de fatorial com entradas negativas
Fazer um programa em C/Python implementando obrigatoriamente uma função de nome fat, com 1 parâmetro n, que, dado um número inteiro n, 
devolva o fatorial de n se n>=0, caso contrário devolva -1. Fazer um programa principal que solicite que o usuário digite um inteiro 
qualquer e usando a funcão fat imprima o fatorial do natural digitado.

Lembrando, a função fatorial fat(n) é definida apenas para os naturais (com o zero), da seguinte forma: fat(0)=1 e fat(n)=n*fat(n-1), n>0. 
Assim, por exemplo, o fatorial de 4 é computado da seguinte forma: fat(4) = 4! = 4.3.2.1 = 24.

Dessa forma, é preciso convencionar o que fazer se o usuário digitar um número inteiro negativo, neste caso seu programa deverá 
imprimir -1 (e.g., se a entrada for: n=-10 => saída -1; n=-21 => saída -1).
"""

def fat(n):
    s = 1
    i = 1
    if n <0 :
        i = -1
    else:
        while s <= n:
            i *= s
            s += 1
    return i
n = int(input())
fat(n)
print(fat(n))