from lib.exceptions import EmptyException

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=5):
        """Create an empty stack."""
        self._data = [None] * maxlen
        self._maxlen = maxlen
        self._next_add = 0
        self._size = 0
        self._front = 0  # Puntero al elemento más antiguo

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._size == self._maxlen:
            # Si el stack está lleno, reemplazamos el elemento más antiguo
            self._data[self._front] = e
            # Actualizar _next_add para que apunte al siguiente después del nuevo elemento
            self._next_add = (self._front + 1) % self._maxlen
            # Desplazamos el puntero al frente de la pila
            self._front = (self._front + 1) % self._maxlen
        else:
            # Si no está lleno, agregamos el elemento en el siguiente espacio disponible
            self._data[self._next_add] = e
            self._next_add = (self._next_add + 1) % self._maxlen
            self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise EmptyException if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[(self._next_add - 1) % self._maxlen]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise EmptyException if the stack is empty.
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')

        # Decrementar _next_add y usar módulo para ajustar
        self._next_add = (self._next_add - 1) % self._maxlen
        elemento = self._data[self._next_add]
        self._data[self._next_add] = None  # Limpiar el espacio
        self._size -= 1

        return elemento

    def __str__(self):
        pila = [e for e in self._data]
        return str(pila)
if __name__ == '__main__':
  pila = ArrayStack(3)
  print(pila)

  pila.push(10)
  pila.push(20)
  pila.push(30)
  print(pila.is_empty())
  print(len(pila))
  print(pila)

  pila.push(40)
  print(pila)

  print(pila.pop())
  print(pila)
  pila.push(50)
  print(pila)
  pila.push(60)
  print(pila)
  print(pila.pop())
  print(pila)
