class TreeNode:
    def __init__(self,data):
        self.data= data
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.children.append(child)


