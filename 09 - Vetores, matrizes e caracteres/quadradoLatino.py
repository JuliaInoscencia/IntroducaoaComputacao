"""
Verificar se matriz é quadrado latino
Dizemos que uma matriz mat, com n linhas e n colunas, é um quadrado latino se, e somente se, para toda linha (e coluna) i (entre 0 e n-1) 
o vetor formado por essa linha (e coluna) é um vetor de permutação.

Lembrando, um vetor é de permutação, se, e somente se, para todo i (entre 0 e n-1) existir um único j entre 0 e n-1 tal que vet[j]=i 
(ou seja, existe uma única cópia de i no vetor). Exemplos de vetores de permutação de tamanho 3: [0,1,2], [0,2,1], [1,0,2], [1,2,0], 
[2,1,0], [2,0,1]. Na verdade, essas são as únicas 6 opções de vetores de permutação de tamanho 3.

É proibido usar o "operador de pertinência" in (exceto em for i in range...), deve-se usar a leitura de string e decomposição em 
inteiros pois os dados do vetor estão em uma única linha ("vet = list(map(int, input().split()))").
"""

def matriz(n):
    i = 0
    matriz = []
    while i != n:
        vet = list(map(int, input().split()))
        matriz.append(vet)
        i+= 1
    return(matriz)    
def quadlatino(matriz,n):
    m = 0
    j = 0
    sequenc = 0
    perm = 1
    while m != n:
        for i in matriz:
            num = i[m]
            j += 1
            if j > 1:
                if sequenc == num:
                    perm = 0
            sequenc = num
        m += 1
        j = 0
    if perm != 1:
        print('NAO')
    else: 
        print('SIM')
n = int(input())
quadlatino(matriz(n),n)
