from lib.linked_binary_tree import LinkedBinaryTree

def nodos_profundidad_n(arbol, n):
    sum = 0
    nodos = []
    for i in arbol.breadthfirst():
        if arbol.depth(i) == n:
            nodos.append(i.element())
        if arbol.depth(i) > n:
            break
    return nodos

arbol = LinkedBinaryTree()
arbol.add_root(2)
arbol.add_left(arbol.root(), 7)
arbol.add_right(arbol.root(), 5)
arbol.add_left(arbol.left(arbol.root()), 2)
arbol.add_right(arbol.left(arbol.root()), 6)
arbol.add_right(arbol.right(arbol.root()), 9)
arbol.add_left(arbol.right(arbol.left(arbol.root())), 5)
arbol.add_right(arbol.right(arbol.left(arbol.root())), 11)
arbol.add_left(arbol.right(arbol.right(arbol.root())), 4)


print(nodos_profundidad_n(arbol, 3))
