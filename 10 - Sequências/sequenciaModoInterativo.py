"""
Gerar e imprimir o n primeiros termos de uma sequência definida iterativamente

O objetivo desta atividade é implementar uma função para imprimir os n primeiros termos de uma sequência definida de modo iterativo 
(termo si depende de termos anteriores).
Faça um procedimento (função "vazia" - que nada devolve) com um único parâmetro formal, um inteiro n, e que imprima os n primeiros termos 
da sequência si definida por: s1=1, s2=2, si+2=si+1+(si+1+si)/2,∀i>2.
Faça um programa que solicita do usuário um natural n>2 (não precisa verificar a condição) e, invocando a função acima, imprima os n 
primeiros termos da sequência si definida acima.
"""

def si(n):
    i = 2
    x = 2
    lista = [1, 2]
    while i < n:
        si = (lista[x-1] + (lista[x-1] + lista[x-2])/2)
        lista.append(si)
        x += 1
        i += 1
    print(lista)


n = int(input())
si(n)
