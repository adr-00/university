from lib.array_queue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        __slots__='_element','_parent','_left','_right'
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
        def element(self):
            return self._element

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self): # devuelve raiz
        return self._root

    def parent(self,node): # devuelve el padre de node
        return node._parent

    def num_children(self,node): #numero hijos de node
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def children(self,node): #iteracion sobre los hijos de un nodo
        if node._left is not None:
            yield self.left(node)
        if node._right is not None:
            yield self.right(node)

    def __len__(self): #numero total de elementos en el arbol
        return self._size

    def left(self,node):
        return node._left

    def right(self,node):
        return node._right

    def sibling(self,node):
        parent = self.parent(node)
        if parent is None:
            return None
        else:
            if node is self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def is_root(self,node):
        return node is self.root()

    def is_leaf(self,node):
        return self.num_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self,node):
        if self.is_root(node):
            return 0
        else:
            return 1+self.depth(self.parent(node))

    def _height2(self,node):
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(node))

    def height(self,node=None):
        if node is None:
            node = self.root()
        return self._height2(node)

    def add_root(self,e): #pone e en el raiz de un arbol vacio y devuelve el nodo
        if self._root is not None: 
            raise ValueError('Root existe')
        self._root = self.Node(e)
        self._size = 1
        return self._root

    def add_left(self,node,e):# crea hijo izquierda de node y almacena e, devuelve su nodo
        if node._left is not None: 
            raise ValueError('Izquierda existe')
        self._size += 1
        node._left = self.Node(e,node)
        return node._left

    def add_right(self, node, e):# crea hijo derecha de p y almacena e, devuelve su nodo
        if node._right is not None: 
            raise ValueError('Derecha existe')
        self._size += 1
        node._right = self.Node(e, node)
        return node._right

    def replace(self,node,e):#reemplaza el elemento de node con e y devuelve el antiguo elemento
        ele = node._element
        node._element = e
        return ele

    def delete(self, node):
        # Elimina el nodo y lo sustituye con su hijo si tiene alguno. 
        # Devuelve el elemento almacenado en el nodo. Error si tiene dos hijos.
        if self.num_children(node) == 2: 
            raise ValueError('node tiene dos hijos')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convención para un nodo que ya no es válido
        return node._element

    def attach(self, node, t1, t2):
        # Incorpora T1 y T2 como hijos izquierda y derecha de node y restablece T1 y T2 como árboles vacíos. 
        # Error si node no es una hoja. 
        if not self.is_leaf(node): 
            raise ValueError('El nodo debe ser una hoja')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Los arboles no son del mismo tipo')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def __iter__(self):
        for node in self.nodes():
            yield node.element()

    def nodes(self):
        return self.preorder() # se podría seleccionar otro recorrido

    def preorder(self):
        if not self.is_empty():
            for node in self._subtree_preorder(self.root()):
                yield node

    def _subtree_preorder(self,node):
        yield node
        for c in self.children(node):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for node in self._subtree_postorder(self.root()):
                yield node
    
    def _subtree_postorder(self,node):
        for c in self.children(node):
            for other in self._subtree_postorder(c):
                yield other
        yield node

    def inorder(self):
        if not self.is_empty():
            for node in self._subtree_inorder(self.root()):
                yield node
    
    def _subtree_inorder(self,node):
        if self.left(node) is not None:
            for other in self._subtree_inorder(self.left(node)):
                yield other
        yield node
        if self.right(node) is not None:
            for other in self._subtree_inorder(self.right(node)):
                yield other

    def breadthfirst(self):
        if not self.is_empty():
            q = ArrayQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                node = q.dequeue()
                yield node
                for c in self.children(node):
                    q.enqueue(c)
    
