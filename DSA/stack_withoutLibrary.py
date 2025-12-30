class Stack:
    def __init__(self):
        self.data = []     

    def push(self, item):
        self.data.append(item)   

    def pop(self):
        if not self.data:
            return None         
        return self.data.pop()  

    def peek(self):
        if not self.data:
            return None
        return self.data[-1]    

    def is_empty(self):
        return len(self.data) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack after pushes:", s.data)
print("Popped item:", s.pop())
print("Top item:", s.peek())
print("Is stack empty?", s.is_empty())
print("Final Stack:", s.data)

