"""
Laço - Soma de positivos e negativos (inteiros) até digitar 0
Construa um programa que lê uma sequência de números inteiros, acumulando a soma de todos os valores que forem positivos e, separadamente!, 
a soma de todos os que forem negativos. A sequência de entradas é encerrada pelo número 0 e, ao terminar, o programa deve imprimir 
primeiro a soma dos números positivos e depois a soma dos números negativos.
"""
pos = 0
neg = 0
n = 1
while n != 0:
    n = int(input())
    if n > 0:
        pos = pos + n
    else:
        neg = neg + n
print(pos,neg)