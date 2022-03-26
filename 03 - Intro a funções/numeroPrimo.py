"""
Funções: Laço simples - Descubra se um inteiro é primo via função
Construa uma função de nome primo, com um parâmetro inteiro n e que devolva 1, se n for primo e 0 em caso contrário. Fazer um programa 
principal deve solicitar que o usuário digite um natural n>0 e, obrigatoriamente usando a função primo com este valor, e de acordo com o 
resultado imprimir 1 se o valor digitado for primo e 0 em caso contrário. Ou seja, nem a entrada e nem a saída de dados deve estar em primo(...).

Atenção: Esta é uma atividade para exercitar o conceito de funções, assim será necessário que implemente uma função que NÃO tenha comandos 
de entrada de dados nela (os dados tem que ser providenciados por quem a invoca). Aqui deve-se usar obrigatoriamente como nome para as 
função primo(n)
"""
def primo(n):
    i = 2
    s = 2
    if n == 2:
        i = 1
    else:
        if n > 2:
            while s < n:
                if n%s == 0:
                    i = 0
                    s = n
                else:
                    i = 1
                    s += 1
        else:
            i = 0
    return i
n = int(input())
print(primo(n))