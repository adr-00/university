from lib.exceptions import EmptyException
from lib.array_stack import ArrayStack
from ejercicio3 import LinkedBinaryTree

def calcular_indentacion(linea):
    return int(linea.count(' ')/4)

def texto_a_arbol(TEXTO):
    with open(TEXTO, "r", encoding='utf-8') as texto:
        lineas = [linea.rstrip('\n') for linea in texto.readlines()]

    lineas = [linea for linea in lineas if linea.strip()]
    if not lineas:
        raise EmptyException("El archivo está vacío")

    indentaciones = [calcular_indentacion(linea) for linea in lineas]

    arbol = LinkedBinaryTree()
    root = arbol.add_root(lineas[0])
    stack = ArrayStack()
    stack.push(root)
    prev_ind = 0

    for i in range(1, len(lineas)):
        act_ind = indentaciones[i]
        linea = lineas[i].lstrip('\t')

        while act_ind < prev_ind:
            stack.pop()
            prev_ind -= 1

        if act_ind > prev_ind:
            parent = stack.top()
            nuevo_nodo = arbol.add_left(parent, linea)
            stack.push(nuevo_nodo)
            prev_ind = act_ind

        elif act_ind == prev_ind:
            stack.pop()
            parent = stack.top()
            nuevo_nodo = arbol.add_right(parent, linea)
            stack.push(nuevo_nodo)
            prev_ind = act_ind
    return arbol

if __name__ == "__main__":
    arbol = texto_a_arbol('texto.txt')
    print(arbol)    