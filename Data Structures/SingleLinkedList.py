class Node:
    def __init__(s,data,next):
        s.data=data
        s.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def get_length(self):
        itr=self.head
        count=0
        while itr.next:
            count+=1
            itr=itr.next
        return count
    def insert_at_pos(self,data,index):
        if index<0 or index>self.get_length()  :
            raise Exception('Invalid Index Position!')
        if index==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            count+=1
            itr=itr.next
    def print(self):
        if self.head is None:
            print('Empty linked list')
            return
        llt=''
        itr=self.head
        while itr:
            llt+=str(itr.data)+'-->'
            itr=itr.next
        print(llt)

    def delete_at_begining(self):
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next

    def delete_at_end(self):
        if self.head.next is None:
            self.head=None
            return
        itr=self.head
        c=0
        while c!=self.get_length()-2:
            itr=itr.next
            c+=1
        itr.next=None
    def delete_at_pos(self,index):
        if index<0 or index>self.get_length():
            raise Exception('Invalid index to delete the element')
        itr=self.head
        c=0
        while c!=index-1:
            itr=itr.next
            c+=1
        itr.next=itr.next.next

    def insert_element_at_value(self,after,value):
        try:
            index=self.search(after)
            self.insert_at_pos(value,index)
        except Exception as e:
            pass

    def search(self,data):
        if self.head is None:
            print('List is empty')
            return
        itr=self.head
        c=0
        while itr:
            if itr.data==data:
                print(f'data {data} found at index position {c}')
                return c
                break
            c+=1
            itr=itr.next
        else:
            print('Element not found in list')

    def update_at_value(self,value,updatedval):
        if self.head is None:
            print("List is empty to update value")
            return
        itr=self.head
        c=0
        while itr:
            if itr.data==value:
                itr.data=updatedval
                print(f'Value updated from {itr.data} to {updatedval} at index {c}')
                break
            c+=1
            itr=itr.next
        else:
            print(f'unable to update,Value {value} not found in list')

    def update_by_index(self,index,updateval):
        if index<0 or index>self.get_length():
            raise  Exception('Invalid Index Position to update value by index')
        itr=self.head
        c=0
        while itr:
            if index==c:
                temp=itr.data
                itr.data = updateval
                print(f'data at index position {c} updated to {updateval} from {temp}')
                break
            c+=1
            itr=itr.next

    # insert multiple elements at once at end of linked list
    def insert_elemnts_at_end(self,data):
        for d in list(data):
            self.insert_at_end(d)
    def insert_elemnts_at_begining(self,data):
        for d in data[::-1]:
            self.insert_at_begining(d)
    def delete_all(self):
        self.head=None
    def swap_element_at_index(self,index1,index2):
        itr1=self.head
        itr2=self.head
        c1,c2=0,0
        while itr1:
            if c1==index1:
                break
            itr=itr.next
            c1+=1
        while itr2:
            if c2==index2:
                break
            itr2=itr2.next
            c2+=1
        t=itr1.data
        itr1.data=itr2.data
        itr2.data=t


    def merge_with(self,list2):

        itr=list2.head
        while itr:
            self.insert_at_end(itr.data)
            itr=itr.next
        print('merging done!')
        return
    def remove_by_value(self,value):
        try:
            index=self.search(value)
            self.delete_at_pos(index)
        except Exception as e:
            pass
ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(4)
ll.insert_at_begining(3)
ll.insert_at_begining(2)
ll.insert_at_begining(1)
ll.insert_at_begining(0)
ll.insert_at_end(10)
ll.print()
print(ll.get_length())
ll.delete_at_begining()
ll.print()
ll.update_at_value(2,'two')
ll.print()
ll.update_by_index(1,2)
ll.print()
print('--------------------------')
ll.swap_element_at_index(0,1)
ll.print()
print(ll.get_length())
ll1=LinkedList()
ll1.insert_elemnts_at_end([11,22,33,44])
ll1.insert_elemnts_at_begining([0,1,2,3])
ll.print()
ll1.print()
ll.merge_with(ll1)
ll.print()
ll.insert_element_at_value(120,'last')
ll.print()
ll.remove_by_value(323)
ll.print()
ll.insert_at_pos(23, 2)
ll.print()