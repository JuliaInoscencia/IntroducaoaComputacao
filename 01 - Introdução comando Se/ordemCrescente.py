"""
Introdução - seleções encaixadas, ordenar decrescente 3 inteiros
Construa um programa que recebe três (3) números inteiros e os imprima em ordem decrescente.
"""
n1=int(input())
n2=int(input())
n3=int(input())
if n1>=n2 and n2>=n3:
    print(n1,n2,n3)
if n1>=n2 and n3>=n2 and n1>=n3:
    print(n1,n3,n2)
if n3>=n1 and n3>=n2 and n1>=n2:
    print(n3,n1,n2)
if n3>=n1 and n3>=n2 and n2>=n1:
    print(n3,n2,n1)
if n2>=n1 and n2>=n3 and n3>=n1:
    print(n2,n3,n1)
if n2>=n1 and n2>=n3 and n1>=n3:
    print(n2,n1,n3)