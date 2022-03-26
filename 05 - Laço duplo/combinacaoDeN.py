"""
Fazer um programa que, após o usuário digitar N e k (nessa ordem), calcula C(N,k) (combinação de N, k-a-k).Lembrando, a função fatorial 
fat(n) é definida apenas para os naturais (com o zero), da seguinte forma: fat(0)=1 e fat(n)=n*fat(n-1), n>0.
Assim, por exemplo, o fatorial de 4 é computado da seguinte forma: fat(4) = 4! = 4.3.2.1 = 24.
"""

N = int(input())
k = int(input())
fat = 1
c = N-k
fat2 = 1
fat3 = 1
for i in range(1,N+1):
   fat *= i
for i in range(1,c+1):
    fat2 *= i
for i in range(1,k+1):
    fat3 *= i
s = int(fat/((fat2)*fat3))
print(s)