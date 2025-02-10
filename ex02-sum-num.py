# Exercício 2: Soma de Números em uma Lista Aninhada

'''
Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
soma de todos os números em uma lista, mesmo que os números estejam dentro de
sublistas (listas aninhadas).

Exemplo de Entrada:
soma_lista_aninhada([1, [2, 3], [4, [5]]])
Saída Esperada:
15 # (1 + 2 + 3 + 4 + 5)

Dica: Verifique se o elemento atual é uma lista ou um número para decidir se deve
continuar a recursão.
'''

def soma_lista_aninhada(lista: list) -> int:
    """Calcula a soma de todos os números em uma lista, mesmo que os números estejam dentro de sublistas.

    Args:
        lista (_type_): A lista poder conter números e sublistas com mais números.

    Returns:
        _type_: A soma de todos os números na lista.
    """
    if not lista:
        return 0
    first = lista[0]
    
    if isinstance(first, list):
        return soma_lista_aninhada(first) + soma_lista_aninhada(lista[1:])
    else:
        return first + soma_lista_aninhada(lista[1:])
          
print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))

'''
Fiz um caso base para quando a lista estiver vazia, retornando 0.

Verifiquei se o primeiro item da lista é uma sublista. Se for, a função chama a si mesma para somar os valores dentro dessa sublista e depois soma com o restante da lista usando slice.

Caso contrário, a função soma o valor do primeiro item com a soma do resto da lista, chamando a função recursivamente até que todos os itens sejam somados.
'''
    