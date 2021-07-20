class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]

    def getHash(self,key):
        s=0
        for word in key:
            s+=ord(word)
        return s%self.MAX
    def __setitem__(self, key, value):
        h=self.getHash(key)
        found=False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,value)
                found=True
        if not found:
            self.arr[h].append((key,value))
    def __getitem__(self, key):
        h=self.getHash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h=self.getHash(key)
        for i,e in enumerate(self.arr[h]):
            if e[0]==key:
                del self.arr[h][i]




t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
t['harsh']=45
t['hsrah']=555
t['harhs']=123
t['harsh']=555
print(t.arr)
print(t['march 6'])