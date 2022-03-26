"""
Dado n e n valores inteiros, imprimir os n valores inteiros em ordem inversa
O objetivo desta atividade é apenas ilustrar o uso de vetores. O usuário deverá digitar um valor natural n (supor maior que zero) e depois 
digitar n valores inteiros. Após todos os n valores inteiros terem sido digitados, seu código deverá imprimir esses n valores digitados, 
mas em ordem inversa. Desse modo é essencial manter registro de todos os valores digitados, logo é necessário o uso de um vetor.
"""

n = int(input())
i = 0
vet = []
while i < n:
    item = int(input())
    vet.append(item)
    i += 1
for i in vet[::-1]:
    print(i)