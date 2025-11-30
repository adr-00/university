from lib.exceptions import EmptyException

class Full(Exception):
    pass
class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self, maxlen=5):
    """Create an empty stack."""
    self._data = [] * maxlen        #Lista vacia con reserva de 5 elementos
    self._maxlen = maxlen
    self._size = 0                      # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size                   #Devolvemos el nuevo atributo que es la longitud

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0              #Utilizamos la longitud para ver si es cero

  def push(self, e):
    """Add element e to the top of the stack."""
    if self._size < self._maxlen:       #Aqui igual
        self._data.append(e)
        self._size += 1                 #Le sumamos al tamaño 1
    else:
        raise Full("La pila esta llena")                 # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyException('Stack is empty')
    return self._data[self._size - 1]                 #El ultimo elemento es el tamaño menos 1 por que empieza desde cero

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyException('Stack is empty')
    elemento = self._data[self._size - 1]
    self._size -= 1                                 #Le quitamos uno al eliminar elemento
    return elemento