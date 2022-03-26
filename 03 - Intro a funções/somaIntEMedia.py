"""
Funções: Introdução ao uso de funções: somar inteiros e média
Construa um programa com funções de nome soma e media, ambas com 2 parâmetros formais do tipo int, que devolvem respectivamente, a soma 
dos parâmetros e sua média. As funções devem ter 2 parâmetros inteiros, como em soma(a, b) e media(a, b). Seu programa principal deverá 
receber do usuário 2 números inteiros, invocar primeiro a funcão soma com eles (como parâmetros efetivos) e imprimir o resultado devolvido 
(sua soma). Depois deve invocar media, também usando as duas entradas como parâmetros efetivos, e, com o valor devolvido, imprimir a média 
aritmética. Claro que deve-se invocar as funções.
"""

def soma(a,b):
    s = a + b
    return s
def media(a,b):
    m = (a+b)/2.0
    return m
def main ():
    a = int(input())
    b = int(input())
    soma(a,b)
    media(a,b)
    print(soma(a,b),media(a,b))
main()