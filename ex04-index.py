# Exercício 4: Encontrar o Índice do Maior Elemento
'''
Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
índice do maior elemento em uma lista.

Exemplo de Entrada:

indice_maior_elemento([1, 5, 3, 9, 2])
Saída Esperada: 3 # O maior elemento é 9, que está no índice 3
'''
def indice_maior_elemento(lista):
    """Encontra o índice do maior elemento em uma lista de forma recusiva.

    Args:
        lista (_type_): Lista de números inteiros.

    Returns:
        _type_: O índice do maior elemento na lista.
    """
    if len(lista) == 1:
        return 0
    
    indice_resto = indice_maior_elemento(lista[1:])
    
    if lista[0] > lista[indice_resto + 1]:
        return 0
    else:
        return indice_resto + 1


teste = [1, 5, 3, 9, 2]
print(indice_maior_elemento(teste))  

'''
Fiz um caso base para quando a lista tiver apenas um elemento, ou seja vamos remover todos os elementos até que só tenha um elemento evitando assim um loop infinito.

A função chama a si mesma recursivamente com o restante da lista lista[1:] para encontrar o índice do maior elemento.

Depois, comparo o primeiro item da lista com o maior item do restante da lista. Se o primeiro item for maior, a função retorna 0 (indicando que o maior elemento é o primeiro). Caso contrário, a função retorna o índice do maior elemento encontrado na sublista, ajustado com +1 para considerar a posição original da lista. espero que tenha conseguido me explicar.

Este código vai retornar 3 para o exemplo [1, 5, 3, 9, 2], pois o maior elemento é 9, que está no índice 3 e sabemos que o indice começa em 0, então 3 + 1 = 4.
'''