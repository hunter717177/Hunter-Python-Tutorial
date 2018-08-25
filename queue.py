class Queue:
    
    def __init__(self):
        self.store = {}
        self.min = 0
        self.max = 0
        
    def enqueue(self, value):
        self.store[self.max] = value
        self.max +=1
        
    def dequeue(self):
        oldest = self.store[self.min]
        del self.store[self.min]
        self.min +=1
        return oldest

x = Queue()
x.enqueue(10)
print(x.store)
x.enqueue(5)
print(x.store)
print(x.store, x.dequeue())