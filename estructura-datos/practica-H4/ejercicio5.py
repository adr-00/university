from lib.linked_binary_tree import LinkedBinaryTree

def sum_impar(arbol):
    sum = 0
    for i in arbol.nodes():
        if arbol.num_children(i) == 1 and i.element()%2 != 0:
            sum += i.element()
    return sum

arbol = LinkedBinaryTree()
arbol.add_root(2)
arbol.add_left(arbol.root(), 7)
arbol.add_right(arbol.root(), 5)
arbol.add_left(arbol.left(arbol.root()), 2)
arbol.add_right(arbol.left(arbol.root()), 7)
arbol.add_right(arbol.right(arbol.root()), 9)
arbol.add_left(arbol.right(arbol.left(arbol.root())), 5)
arbol.add_left(arbol.right(arbol.right(arbol.root())), 4)


print(sum_impar(arbol))


