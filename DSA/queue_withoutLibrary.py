class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, val):
        self.data.append(val)
    def dequeue(self):
        if not self.data:
            return None
        return self.data.pop(0)

# Using  queue
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.data)      
print(q.dequeue())  
print(q.data)       
