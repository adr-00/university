# Hay que utilizar un nuevo atributo llamado next to add, que nos dice por donde hay q meter elementos 
#Para esto hay que utilizar el modulo para el contador


from lib.exceptions import EmptyException

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self, maxlen=5):
    """Create an empty stack."""
    self._data = [None] * maxlen
    self._maxlen = maxlen
    self._next_add = 0
    self._size = 0                      # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data[self._next_add] = e
    self._next_add = (self._next_add + 1) % self._maxlen
    if self._size < self._maxlen:
      self._size += 1
      
      
  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyException('Stack is empty')
    return self._data[self._next_add - 1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyException('Stack is empty')
    elemento = self._data[self._next_add - 1]
    self._data[self._next_add - 1] == None
    return elemento
  

if __name__ == '__main__':
  s = ArrayStack(4)
  s.push(5)
  s.push(3)
  print(s.pop())
  s.push(2)
  s.push(8)
  print(s.pop())
  print(s.pop())
  s.push(9)
  s.push(1)
  print(s.pop())
  s.push(7)
  s.push(6)
  print(s.pop())
  print(s.pop())
  s.push(4)
  print(s.pop())
  print(s.pop())
  print("Hola")