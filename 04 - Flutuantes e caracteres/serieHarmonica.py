"""
(float) Dado n, computar a soma dos n primeiros termos da série harmônica
Construa um algoritmo que receba um natural positivo n (n>0) e imprime a soma dos n primeiros termos da série harmônica abaixo definida.

H = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/k + ...

O objetivo dessa atividade é exercitar os conceitos iniciais de programação, portanto não procure uma forma fechada para Hn 
(deve-se implementar um laço)."""

n = int(input())
k=1
h=0
s=1
while k <= n:
    h+=1/(k)
    k+=1
print(h)
    