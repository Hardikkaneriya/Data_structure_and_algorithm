class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:    
    def createNode(self,data):
        return Node(data)
        
    
    def insert(self, node , data):
        if node is None:
            return self.createNode(data)
        if data < node.data :   
            node.left= self.insert(node.left,data)
        else:
            node.right = self.insert(node.right, data)
        return node    
    
    #inorder traverse (left , root , right) will always 
    #print sorted array
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data , end =" ")
            self.traverse_inorder(root.right)


if __name__ == "__main__":
    l= BinaryTree()
    root=l.createNode(5)
    l.insert(root, 2)
    l.insert(root, 10)
    l.insert(root, 7)
    l.insert(root, 15)
    l.insert(root, 12)
    l.insert(root, 20)
    l.insert(root, 30)
    l.insert(root, 6)
    l.insert(root, 8)
    l.traverse_inorder(root)

