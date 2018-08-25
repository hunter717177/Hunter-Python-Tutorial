"""Create Queue class"""
class Queue:
    """Creates Queue Class"""

    def __init__(self):
        self.store = {}
        self.min = 0
        self.max = 0

    def enqueue(self, value):
        """adds to queue"""
        self.store[self.max] = value
        self.max += 1

    def dequeue(self):
        """returns first value in queue and removes it from queue"""
        oldest = self.store[self.min]
        del self.store[self.min]
        self.min += 1
        return oldest

X = Queue()
X.enqueue(10)
print(X.store)
X.enqueue(5)
print(X.store)
print(X.store, X.dequeue())
