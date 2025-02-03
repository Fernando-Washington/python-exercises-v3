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

def soma_lista_aninhada(lista):
    if not lista:
        return 0
    first = lista[0]
    
    if isinstance(first, list):
        return soma_lista_aninhada(first) + soma_lista_aninhada(lista[1:])
    else:
        return first + soma_lista_aninhada(lista[1:])
          
print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))
    