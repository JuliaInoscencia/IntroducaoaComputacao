"""
Introdução seleção - operador resto da divisão
Construa um programa que recebe um número inteiro não negativo (não precisa testar) e verifique se ele é par ou ímpar. Se for par seu 
programa deve imprimir 1, caso contrário (é ímpar) deve imprimir 0. Note que um único comando do tipo seleção basta!
"""
n=int(input())
n=n%2
if n == 0:
    print("1")
else:
    print("0")