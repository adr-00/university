# imprimimos arbol usando recorrido preorden

from lib.linked_binary_tree import LinkedBinaryTree

# Prints a tree using proper indentation
def escritura_arbol(T,node,d):
    print(2*d*' '+str(node.element()))
    
    if not T.is_leaf(node):
        if T.left(node) is not None:
            escritura_arbol(T,T.left(node),d+1)
        else:
            print(2*(d+1)*' '+'None')
            
        if T.right(node) is not None:
            escritura_arbol(T,T.right(node),d+1)
        else:
            print(2*(d+1)*' '+'None')


if __name__ == '__main__':

    T = LinkedBinaryTree()
    r = T.add_root('a')
    T.add_right(r,'c')
    T.add_left(r,'b')
    # ...

    escritura_arbol(T,T.root(),0)
