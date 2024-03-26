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

    #preorder traverse (root , left , right)
    def traverse_preorder(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    #postorder traverse (left , right , root)
    def traverse_postorder(self,root):
        if root is not None:
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
            print(root.data, end=" ")

if __name__ == "__main__":
    l=[5,4,2,10]
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
    l.traverse_preorder(root)
    l.traverse_postorder(root)

