class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        space=' '*self.get_level()*3
        prefix=space+"|__"if self.parent else""
        print(prefix+self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()
    def get_level(self):
        lvl=0
        p=self.parent
        while p:
            lvl+=1
            p=p.parent
        return lvl



def genrateaTree():
    root = TreeNode('Electronics')

    laptop=TreeNode('laptop')
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('surface'))
    laptop.add_child(TreeNode('thinkpad'))

    cellphone=TreeNode('cellphone')
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('samsung'))
    cellphone.add_child(TreeNode('Pixel'))
    
    tv=TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))
    
    root.add_child(tv)
    root.add_child(laptop)
    root.add_child(cellphone)
    return root

root=genrateaTree()
root.print_tree()
