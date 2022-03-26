"""
Testar se caractere é letra, se minúscula ou se maiúscula

Fazer um programa que testa se caracteres digitados são letras e, nesse caso, verifica ainda se são minúsculas ou se maiúsculas. 
O programa deve interromper sua execução quando for digitado o caractere zero (0). Para cada caractere digitado, se ele não for letra 
imprimir -1, se for letra minúscula imprimir 1 e se for maiúscula imprimir 2.

Pode supor que os caracteres digitados, quando forem letras, todos eles serão letras SEM acento (portanto seguindo o padrão de 
codificação ASCII (American Standard Code for Information Interchange).

Dica 1: Em qualquer mapa de caracteres, aqueles que implicam algum tipo de ordem (e.g. crescente) seguem um padrão (crescente) de 
representação, assim o caractere 'B' tem código uma unidade acima do código de 'A' (o mesmo para letras minúsculas e para os dígitos).
Dica 2: No padrão ASCII, o caractere 'A' tem código 65 e o caractere '0' (dígito 0), tem código 48.
"""

n = 1
while n != 0:
    n = input()
    c = ord(n)
    if c < 58:
        print(-1)
    elif c > 96:
        print(1)
    else:
        print(2)