"""
Dada uma "string" de dígitos, converter para valor numérico correspondente
Nesta atividade você deve, basicamente, implementar o algoritmo que computa o valor de um número em base decimal. O programa usará uma 
cadeia de caracteres (string) composta pelo caractere 'N' e seguida exclusivamente por dígitos (0, 1, 2 até 9), para gerar uma variável 
numérica e ao final imprimir esse valor numério e seu dobro. Para isso:

1. Implemente uma função de nome (e único parâmetro) converte(vetc[]) que, a partir do parâmetro (que deve ser uma string com 'N' antes de
cada dígito válido), computa o decimal correspondente ao valor numérico dos dígitos sem o marcador 'N' e devolve esse número e seu dobro.

2. No programa principal: o usuário deverá digitar uma string com uma sequência de caractere (e.g. 'N') e seguida um dígito; invocar a 
função  converte(...) acima, guardando o valor em uma variável; e por último, imprimir essa variável e o dobre dela.
"""

def converte(n):
    n = n
    cont = len(n)
    s =int(n[1:cont:2])
    return s
n = str(input())
s = converte(n)
print(s, s*2)

    