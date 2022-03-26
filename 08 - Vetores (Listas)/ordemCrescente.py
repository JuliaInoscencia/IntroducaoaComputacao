"""
Determinar se um vetor está em ordem crescente
1. Implementar uma função de nome determineSeOrdenado que recebe como parâmetros um inteiro n e vetor de inteiros vet e que devolve 1 se 
os elementos em vet[] estão em ordem crescente e 0 em caso contrário (ou seja, se vet[0] <vet[1] < ... < vet[n-1],  devolve 1 e em 
qualquer outra configuração devolve 0).

2. Fazer um programa principal no qual o usuário digita n>0, seguido de n valores inteiros que são armazenados em um vetor (que poderá ter 
até 40 elementos). Usando a função do item 1, seu programa deve imprimir 1 se o vetor está em ordem crescente e 0 em caso contrário.
"""

def determineSeOrdenado(n,vet):
    i = 1
    aux = 0
    o = 0
    while i < n:
        if vet[aux] <= vet[aux+1]:
            o = 1
        else:
            o = 0
        aux += 1
        i += 1 
    return o
n = int(input())
vet = []
i = 0
while i < n:
    item = int(input())
    vet.append(item)
    i +=1
o = determineSeOrdenado(n,vet)
if n == 1:
    o = 1
print (o)
    