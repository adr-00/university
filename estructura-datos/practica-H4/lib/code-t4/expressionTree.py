from Linked_Stack import LinkedStack
from linkedbinarytrees import LinkedBinaryTree
import lecturaEscritura
import operator

def buildParsetree(expres):
    lisexp = list(expres)
    pila = LinkedStack()
    tree = LinkedBinaryTree()
    actual = tree.add_root('')
    pila.push(actual)
    for i in lisexp:
        if i == '(':
            pila.push(actual)
            actual = tree.add_left(actual,'')
        elif i not in '+-*/)':
            tree.replace(actual,i)
            actual = pila.pop()
        elif i in '+-*/':
            tree.replace(actual,i)
            nuevo = tree.add_right(actual,'')
            pila.push(actual)
            actual = nuevo
        elif i == ')':
            actual = pila.pop()
        else:
            raise ValueError("Operador desconocido "+i)
    return tree

def evaluar(t,node): # debe tomar el nodo raiz inicialmente
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    left = t.left(node)
    right = t.right(node)

    if left and right:
        fn = opers[node.element()]
        return fn(evaluar(t,left),evaluar(t,right))
    else:
        return int(node.element())

if __name__ == '__main__':

    t = buildParsetree("((2+5)*(3+8))")

    for node in t.nodes():
        print(node.element())

    print('Resultado =',evaluar(t,t.root()))

    t = buildParsetree("((2-5)*(3+8))")

    for node in t.nodes():
        print(node.element())

    print('Resultado =',evaluar(t,t.root()))

