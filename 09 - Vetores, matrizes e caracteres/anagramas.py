"""
Faça uma função que testa se duas palavras fornecidas em vetores de caracteres (strings) são anagramas. Escolha como ela informará ao 
programa principal. A função NÂO deve ter nem comandos de leitura e nem de impressão.

No programa principal, o usuário deverá digitar um natural n (n>0) seguido de 2 vetores de caracteres (representando as palavras), cada 
um com n caracteres, então usar a função acima citada parar imprimir "ANAGRAMAS" se as palavras o forem ou "NAO" em caso contrário.

Deve-se ignorar diferenças entre maiúsculas e minúsculas, i.e., 'a' e 'A' devem ser consideradas iguais. Pode-se supor que aparecerão 
apenas letras entre 'a' e 'z' ou entre 'A' e 'Z'. Dica: Usar a boa ordem no código ASCII para converter A para a (ou vice-versa): ASCII 
de 'A' é 65 e o de 'a' é 97, logo de 'B' é 66 e de 'b' é 98.

É proibido usar o "operador de pertinência" in (que é uma implementação de um algoritmo de busca para identificar pertinência de elemento 
em conjunto) ou qualquer outra função que simplifique o problema (como sorted(.)). A razão é que a parte mais importante do exercício é 
precisamente implementar um algoritmo para identificar algo semelhante à pertinência.
"""

def anagrama(n,lista1,lista2):
    m = n - 1
    x = 0
    a = 0
    verdadeiro = 1
    while x != m:
        while a != n:
            if lista1[x] != lista2[a]:
                a += 1
                verdadeiro = 0
            else:
                del(lista2[a])
                verdadeiro = 1
                n -= 1
                a = 0
                x += 1
        x = m        
    return verdadeiro           
            
n = int(input())
i = 0
lista1 = []
lista2 = []
while i != 2:
    k = 0
    while k != n:
        if i == 0:
            a = input()
            if (ord(a)) > 96:
                lista1.append(a)
            else:
                b = chr((ord(a)+32))
                lista1.append(b)
            k += 1
        else:    
            a = input()
            if (ord(a)) > 96:
                lista2.append(a)
            else:
                b = chr((ord(a)+32))
                lista2.append(b)
            k += 1
    i += 1
resultado = anagrama(n,lista1,lista2)
if resultado != 0:
    print("ANAGRAMAS")
else:
    print("NAO")