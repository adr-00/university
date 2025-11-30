from lib.linked_binary_tree import LinkedBinaryTree
from ejercicio1 import texto_a_arbol


T = texto_a_arbol("texto.txt")


def clonar(T, node):
    nuevo_arbol = LinkedBinaryTree()
    if T.is_root(node):
        nuevo_arbol.add_root(node)
    elif T.is