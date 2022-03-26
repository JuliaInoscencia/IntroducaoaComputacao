"""
Introdução - ler dois inteiros e trocar os conteúdos das variáveis
Construa um algoritmo utilizando apenas 3 variáveis de nomes: a, b e aux. Seu algoritmo deve: solicitar que o usuário digite 2 valores 
(inteiros), armazenando o primeiro em a e o segundo em b; trocar o conteúdo armazenado na variável a com o de b (usar a auxiliar); 
finalmente imprimir o valor de a e de b, nesta ordem!
"""
a=int(input())
b=int(input())
aux=a
a=b
b=aux
print(a,b)