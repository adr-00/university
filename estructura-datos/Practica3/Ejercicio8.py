from lib.exceptions import EmptyException

class Linked_Queue:
  class _Empty(Exception):
    pass
  class _Node:
    __slots__ = "_element", "_next"
    def __init__(self, e, next):
      self._element = e
      self._next = next
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise EmptyException('Queue is empty')
    return self._head._element

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise EmptyException('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == 0:
      self._head = self._Node(e, None)
      self._tail = self._head
    else:
      newest = self._Node(e, None)
      self._tail._next = newest
      self._tail = newest
    self._size += 1

  def _recorrido(self):
      r = self._head
      while r is not None:
        yield r._element
        r = r._next

  def __iter__(self):
      return self._recorrido()

  def __str__(self):
    c = ""
    for e in self:
      c += str(e) + " "
    return c

if __name__ == "__main__":
  Q = Linked_Queue()
  Q.enqueue(5)
  Q.enqueue(3)
  Q.enqueue(2)
  Q.enqueue(8)
  Q.enqueue(9)
  Q.enqueue(1)
  Q.enqueue(4)
  print(Q)
  print(Q.dequeue())
  print(Q.dequeue())
  print(Q.dequeue())
  print(Q.dequeue())
  print(Q.dequeue())
  print(Q.dequeue())
  print(Q.dequeue())
