# Exercício 3: Contar Caracteres em uma String

'''
Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
caractere c aparece na string s.

Exemplo de Entrada:

contar_caracteres("banana", "a")
Saída Esperada: 3
'''
def contar_caracteres(s: str, c: str) -> int:
    """Conta quantos caracteres 'c' existem na string 's'

    Args:
        s (str): String a ser contada
        c (str): Caractere a ser contado

    Returns:
        int: O número de vezes que o caractere 'c' aparece na string 's'
    """
    if len(s) == 0:
        return 0
    
    count = 1 if s[0] == c else 0
    
    return count + contar_caracteres(s[1:], c)

print(contar_caracteres("banana", "a"))
    
'''
Fiz um caso base para quando a string 's' estiver vazia, retornando 0.

Usei uma variável 'count' que vai ser 1 se o primeiro caractere de 's' for igual ao caractere 'c', e 0 caso contrário.

A função chama a si mesma com o resto da string (sem o primeiro caractere) e vai somando o 'count' até que a string acabe.
'''
