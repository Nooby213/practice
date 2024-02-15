class Queue:
    def __init__(self, maxsize):
        self.size = maxsize
        self.items = [None] * maxsize
        self.rear = self.size
        self.front = 0

    def enQueue(self, item):
        if self.isFull():
            print('Queue is Full!!1')
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        return self.items[self.front]

    def isFull(self):
        return self.front == (self.rear + 1) % self.size

q = Queue(3)
q.enQueue('a')
q.enQueue('b')
q.enQueue('c')
print(q.deQueue())
q.enQueue('d')
print(q.items)
