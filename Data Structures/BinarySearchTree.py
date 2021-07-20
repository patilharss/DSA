class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add to left sub tree
            if self.left:  # if left node is not empty
                self.left.addchild(data)  # bcz self.left is another sub tree
            else:  # if left node is empty
                self.left = BST(data)
        else:
            # add to right of sub tree
            if self.right:  # if right node is present
                self.right.addchild(data)
            else:  # if right node is NOT present
                self.right = BST(data)

    # Traversal method
    def inordertraversal(self):
        elements= []

        # first going through left subtree for in order traversal Left-Root-Right
        if self.left:
            elements +=self.left.inordertraversal()  # calling this function recursively on left subtree
        # Visiting base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements+=self.right.inordertraversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val>self.data:  # traverse through right
            if self.right:
                return self.right.search(val)
            else:
                return False

        if val<self.data:  # traverse through left
            if self.left:
                return self.left.search(val)
            else:
                return False

def BuildTree(ele):
    root=BST(ele[0]) # assigned a first element of list as a root node

    for i in range(1,len(ele)):
        root.addchild(ele[i])
    return root


numbers=[10,1,20,11,56,87,89,21,99]
numtree=BuildTree(numbers)
print(numtree.inordertraversal())
print(numtree.search(99))