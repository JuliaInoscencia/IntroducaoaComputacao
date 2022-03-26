"""
(float) Dado n inteiro e x real, computar x^n
Construa um algoritmo que receba um número natural positivo (n) e valor real x), calcule e imprima o valor de xn. 
(potência de x elevado a n). Utilize apenas os operadores de soma e de produto de 2 inteiros.
"""

n = int(input())
x = float(input())
i = 1
cont = x
while i < n:
    x= x*cont
    i+=1
print(x)