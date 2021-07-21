class Queue:
    def __init__(self):
        self.queue=[]
    def insert(self,val):
        self.queue.insert(0,val)
    def pop(self):
        if self.queue!=[]:
            return  self.queue.pop()
        else:
            return []
    def peek(self):
        if self.queue!=[]:
            return  self.queue[-1]
        else:
            return []
    def isempty(self):
        return  self.queue==[]
    def size(self):
        return  len(self.queue)
q=Queue()
q.insert(1)
q.insert(5)
print(q.peek())
q.pop()
q.pop()
print(q.isempty())