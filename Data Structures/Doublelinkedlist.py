class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertatbegining(self, data):
        node = Node(data, None, self.head)
        self.head = node
        if self.head.next:
            self.head.next.prev=self.head



    def print(self):
        if self.head is None:
            print('empty list')
            return

        itr = self.head
        s = ''
        while itr:
            s += '<--' + str(itr.data) + '-->'
            itr = itr.next
        return s

    def insertatend(self, data):
        if self.head is None:
            self.insertatbegining(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)

    def deleteatbegining(self):
        self.head = self.head.next
        self.head.prev = None

    def deleteatend(self):
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def insertmanyatbegining(self, data):
        for i in list(data)[::-1]:
            self.insertatbegining(i)

    def insertmanyatend(self, data):
        for i in list(data):
            self.insertatend(i)

    def search(self, data):
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        c = 0
        while itr:
            if itr.data == data:
                return c

            itr = itr.next
            c += 1
        return -1

    def getlength(self):
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        c = 0
        while itr:
            c += 1
            itr = itr.next
        return c

    def deleteelement(self, data):

        if self.search(data) == 0:
            self.deleteatbegining()
            return
        if self.search(data) == self.getlength() - 1:
            self.deleteatend()
            return
        itr = self.head
        while itr.next:
            if itr.data == data:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                return
            itr = itr.next
    def insertatindex(self,index,data):
        if index >=0:
            if index==1:
                self.insertatbegining(data)
                return
            # if index==self.getlength():
            #     self.insertatend(data)
            #     return
            itr=self.head
            c=0
            while itr:
                if c==index-1:
                    node=Node(data,itr.prev,itr)
                    itr.prev.next=node
                    itr.prev=node
                c+=1
                itr=itr.next
            else:
                print('Invalid index')



dll = DoubleLinkedList()
dll.insertatbegining(100)
dll.insertatbegining(200)
dll.insertatend(500)
dll.insertatend(999)
print(dll.print())
dll.deleteatbegining()
print(dll.print())
dll.deleteatend()
print(dll.print())
dll.insertmanyatbegining([1, 2, 3, 4, 5])
print(dll.print())
dll.insertmanyatend([9999, 8888, 1000])
print(dll.print())
print(dll.search(100))
print(dll.search('not in list -1'))
dll.deleteelement(500)
print(dll.print())
print(dll.getlength())
dll.deleteelement(1)
print(dll.print())
dll.insertatindex(4,'inserted ')
print(dll.print())
