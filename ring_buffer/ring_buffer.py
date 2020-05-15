class RingBuffer:
    def __init__(self, capacity):
        # self.data = [None for i in range(capacity)]
        self.capacity = capacity
        self.current = 0

        self.storage = [None] * capacity

    def append(self, item):
        # self.data.pop()
        # self.data.append(item)
        if self.capacity > len(self.storage):
            self.storage.append(item)
            self.current += 1
        else:
            self.storage[self.current] = item
            self.current = ((self.current + 1) % self.capacity)

    def get(self):
        # return self.data

        values = []
        for item in self.storage:
            if item is not None:
                values.append(item)
        return values


buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())
buffer.append('d')
print(buffer.get())
buffer.append('e')
buffer.append('f')
print(buffer.get())
print(buffer.get())
