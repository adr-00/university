# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LinkedStack:

    class _Empty(Exception):
        pass

    class _Node:
        __slots__ = 'element','next'
        def __init__(self,e,next):
            self.element = e
            self.next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._iterador = self._head

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,e):
        newest = self._Node(e,self._head)
        self._head = newest
        self._size += 1

    def top(self):
        if (self.is_empty()):
            raise self._Empty('Pila Vacía')
        return self._head.element

    def pop(self):
        if (self.is_empty()):
            raise self._Empty('Pila Vacía')
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        return answer

    # para poder iterar por los elementos de la lista

    # con un generador

    def _recorrido(self):
        r = self._head
        while r is not None:
            yield r.element
            r = r.next

    def __iter__(self):
        return self._recorrido()

    # con iteradores

    '''

    def __iter__(self):
        self._iterador = self._head
        return self

    def __next__(self):
        if self._iterador == None:
            raise StopIteration
        answer = self._iterador.element
        self._iterador = self._iterador.next
        return answer
    '''


if __name__ =='__main__':
    l = LinkedStack()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)

    for e in l:
        print(e)

    


    