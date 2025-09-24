class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data):
        new_node = ListNode(data, self._head)
        self._head = new_node #head osoittamaan uuteen nodeen
        if self._tail is None:
            self._tail = new_node # jos tyhjä tail osoittamaan myös uuteen nodeen
        self._size += 1

    def dequeue(self):
        if self._size == 0: # tyhjä
            return None

        if self._head == self._tail: # vain yksi
            value = self._head.data
            self._head = None
            self._tail = None
            self._size -= 1
            return value


        current = self._head #käydään lista läpi tailiin
        while current.next != self._tail:
            current = current.next

        value = self._tail.data #tallennetaan arvo
        self._tail = current
        self._tail.next = None #poistetaan
        self._size -= 1
        return value

    def __repr__(self):
        values = []
        current = self._head
        while current: #lisätään arvot listaan
            values.append(str(current.data))
            current = current.next
        
        if self._size >1 or self._size <1:
            return f'<Queue ({self._size} elements): [{", ".join(values)}]>'
        else:
            return f'<Queue ({self._size} element): [{", ".join(values)}]>'