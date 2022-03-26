"""
Laço - Soma dos números ímpares (até digitar 0)
Construa um algoritmo que lê uma sequência de números inteiros até que o usuário digite o valor 0 (zero). Seu algoritmo deve, ao final, 
imprimir a soma dos valores ímpares que foram digitados (somar apenas os ímpares).

Atenção: seu programa deve ter apenas um comando de impressão (i.e., deve haver apenas uma única linha com printf ou print e deve ser 
impresso um único valor inteiro).
"""
impar = 0
ent = 1
while ent !=0:
    ent = int(input())
    if ent%2 != 0:
        impar = impar + ent
print(impar)