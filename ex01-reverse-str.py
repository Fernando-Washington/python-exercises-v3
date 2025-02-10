# Exercício 1: Reverter os Caracteres de uma String 

'''
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while).
'''

def reverter_caracteres(s: str) -> str:
    """Inverte os caracteres de uma string recursivamente.

    Args:
        s (str): String a ser invertida

    Returns:
        str: String invertida
    """
    if len(s) == 0:
        return s
    return s[-1] + reverter_caracteres(s[:-1])
print(reverter_caracteres('Ola mundo'))

'''
Fiz um caso base para quando a string estiver vazia, retornando a string vazia.

A função pega o último caractere da string e chama a si mesma com o restante da string sem o último caractere, concatenando esse caractere ao resultado da recursão.

Dessa forma vai continuar até que toda a string tenha sido invertida e quando isso acontecer a função retora a string completa invertida.
'''