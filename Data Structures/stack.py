class Stack:
    def __init__(self):
        self.items=[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        return  self.items.pop()
    def peek(self):
        if len(self.items)>0:
            return self.items[-1]
        else:
            return []
    def isempty(self):
        if self.items==[]:
            return True
        else:
            return False

s=Stack()
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
print(s.isempty())
print(s.peek())
s.pop()
s.pop()
print(s.peek())
print(s.isempty())