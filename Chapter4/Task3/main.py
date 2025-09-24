class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'
        
    def enqueue(self, data):
        self._InboundStack.push(data) # Siirretään arvo inbound
        self._size += 1

    def dequeue(self):
        if len(self._OutboundStack) == 0: #Jos outbound tyhjä
            while len(self._InboundStack) > 0:
                self._OutboundStack.push(self._InboundStack.pop()) ## Siirretään inbound -> outbound
        if len(self._OutboundStack) == 0: # Jos vieläkin tyhjä jono oli tyhjä.
            return None
        self._size -= 1
        return self._OutboundStack.pop()

# Fifo kahden stackin avulla 