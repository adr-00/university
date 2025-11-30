class UnsortedPriorityQueue:

    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __eq__(self, other):
            return self._key == other._key and self._value == other._value

    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))

    def find_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        small = self._data[0]
        for item in self._data:
            if item < small:
                small = item
        return (small._key, small._value)

    def min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        return self.find_min()

    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        (k,v) = self.find_min()
        self._data.remove(self._Item(k,v))
        return (k,v)

    def update(self,v,newkey,val):      # actualizar clave y valor
        for item in self._data:
            if v in item._value:
                item._key = newkey
                item._value = val


if __name__ == '__main__':
    pq = UnsortedPriorityQueue()
    a = pq.add(5, 'a')
    b = pq.add(9, 'b')
    c = pq.add(1, 'c')
    d = pq.add(3, 'd')
    e = pq.add(7, 'e')
    f = pq.add(1, 'f')
    g = pq.add(3, 'g')
    h = print("Longitud : " + str(len(pq)))
    while not pq.is_empty():
        print(pq.min())
        print(pq.remove_min())
    
    