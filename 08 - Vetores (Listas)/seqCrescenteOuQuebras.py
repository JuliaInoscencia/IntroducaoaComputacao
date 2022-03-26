"""
Determinar se um vetor está em ordem crescente, senão quantas quebras
1. Implementar uma função de nome determineSeOrdenado que tenha um vetor de inteiros vet[] como parâmetro e devolve um inteiro k que 
significa o número de quebras não crescente. Usar apenas vet[] como parâmetro.
Devolução k: k=0 significa que a sequência é crescente vet[0] < vet[1] < ...  <vet[n-1] (não precisa ser "estritamente"); k>0 é o número 
de quebras não crescente, i.é., significa que a sequência NÃO é crescente e tem k pares do tipo vet[i-1] > vet[i].

2. Fazer um programa principal no qual o usuário digita n>0, seguido de n valores inteiros que são armazenados em um vetor (que poderá 
ter até 40 elementos). Usando a função do item 1, seu programa deve imprimir sim se o vetor está em ordem crescente e em caso contrário, 
nao k, sendo k o número quebras.
"""

def determineSeOrdenado(vet):
    i = 1
    aux = 0
    k = 0
    while i < n:
        if vet[aux] <= vet[aux+1]:
            k += 0
        else:
            k +=1
        aux += 1
        i += 1
    return k
n = int(input())
vet =[]
i = 0
while i < n:
    item = int(input())
    vet.append(item)
    i +=1
k = determineSeOrdenado(vet)
if k == 0:
    print("sim")
else:
    print(" nao")
    print(k)