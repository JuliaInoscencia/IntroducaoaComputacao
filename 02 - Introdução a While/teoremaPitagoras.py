"""
Seleção - Números Pitagóricos - verificar teorema de Pitágoras
Construa um algoritmo que lê três números naturais como entradas e verifica se esses números são pitagóricos. Três números são pitagóricos 
se o quadrado do maior deles (hipotenusa) é igual a soma do quadrado dos outros dois. Como saída de seu programa imprimir: se pitagóricos, 
o valor 1 e o valor da hipotenusa ao quadrado; se não pitagórico, apenas o valor 0.
Os números são denominados pitagóricos por corresponderem a comprimentos de lados de um triângulo retângulo, ou seja, h² = a² + b².
"""
n1 = int(input())
n2 =int(input())
n3 = int(input())
h = 0
a = 0
b = 0
if n3>=n2 and n3>=n1:
    h = n3
    a = n2
    b = n1
    if h**2 == a**2 + b**2:
        print(1,h**2)
    else:
        print(0)
if n2>=n3 and n2>=n1:
    h = n2
    a = n3
    b = n1
    if h**2 == a**2 + b**2:
        print(1,h**2)
    else:
        print(0)
if n1>=n3 and n1>=n2:
    h = n1
    a = n3
    b = n2
    if h**2 == a**2 + b**2:
        print(1,h**2)
    else:
        print(0)