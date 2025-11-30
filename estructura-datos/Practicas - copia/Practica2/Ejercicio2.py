class EmptyException(Exception):
    pass

class FullExcepcion(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=5):
        """Create an empty stack."""
        self._data = []   
        self._maxlen = maxlen                    # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if len(self._data) < self._maxlen:
            self._data.append(e)
        else:
            raise FullExcepcion("Pila llena")
                        # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1]               # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data.pop()