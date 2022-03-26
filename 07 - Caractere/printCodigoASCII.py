"""
Introdução ao uso de caracteres: dado n e n caracteres, obter seu código ASCII
Construa um programa que receba como entrada um número inteiro n e depois n caracteres, imprimindo os códigos ASCII 
(American Standard Code for Information Interchange) de cada um dos caracteres.
"""

a = int(input())
n = 0
while n != a:
    n = input()
    print(ord(n))