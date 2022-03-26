"""
Seleção - Soma de inteiros representando ângulos internos de um triângulo
Construa um programa que verifica se 3 números podem ou não representar os ângulos de um triângulo. Seu algoritmo deve solicitar que o 
usuário digite os 3 números naturais (representando ângulos em graus) e imprimir: "Sim" e os 3 números na sequência digitada, 
se somarem 180; e "NAO" e a soma dos 3 números em caso contrário.
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1+n2+n3 == 180:
    print("Sim",n1,n2,n3)
else:
    print("NAO",n1+n2+n3)