from lib.exceptions import EmptyException

class ArrayStack:

    def __init__(self, maxlen=5):
        self._data = [None] * maxlen
        self._maxlen = maxlen
        self._next_add = 0
        self._size = 0      

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._data[self._next_add] = e
        self._next_add = (self._next_add + 1) % self._maxlen
        if self._size < self._maxlen:
            self._size += 1

    def top(self):
        if self.is_empty():
            raise EmptyException('La pila esta vacia')
        return self._data[(self._next_add - 1) % self._maxlen]

    def pop(self):
        if self.is_empty():
            raise EmptyException('La pila esta vacia')
        ultimo_elem = (self._next_add - 1) % self._maxlen
        elemento = self._data[ultimo_elem]
        self._data[ultimo_elem] = None  
        self._next_add = ultimo_elem   
        self._size -= 1
        return elemento

    def __str__(self):
        pila = [e for e in self._data]
        return str(pila)
      
  

if __name__ == '__main__':
  pila = ArrayStack(3)
  print(pila)

  pila.push(1)
  pila.push(2)
  pila.push(3)
  print(pila.is_empty())
  print(len(pila))
  print(pila)

  pila.push(4)
  print(pila)

  print(pila.pop())
  print(pila)
  print(pila.top())
  pila.push(5)
  print(pila)
  pila.push(6)
  print(pila)
  print(pila.pop())
  print(pila)
  print(pila.top())
  print(pila.pop())
  print(pila)
  pila.push(7)
  print(pila)
  pila.push(8)
  print(pila)
  print(pila.top())
  pila.push(9)
  print(pila)
  print(len(pila))




