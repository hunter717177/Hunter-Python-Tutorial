class Stack:

    def __init__(self):
        self.store = {}
        self.length = 0

    def push(self, value):   
        self.length += 1
        self.store[self.length] = value

    def pop(self):
        latest = self.store[self.length]
        del self.store[self.length]
        self.length -= 1
        return latest

x = Stack()
x.push(10)
x.push(5
print(x.store)
print(x.store, x.pop())
