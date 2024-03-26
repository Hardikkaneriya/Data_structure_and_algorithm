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

    def height(self, root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right)) + 1

    #this function will print all nodes at base level 
    def levelOrder(self, root):
        q=[]
        q.append(root)
        while len(q) != 0 :
            root = q.pop(0)
            print(root.data , end = " ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
    
    #this code is not working for this class it is 
    #implemented for another leetcode problem for understanding
    def topView(self,root):
        q=[]
        dic={}
        root.level = 0
        q.append(root)
        while len(q) != 0 :
            root = q.pop(0)
            if root.level not in d:
                d[root.level] = root.data
            if root.left is not None:
                q.append(root.left)
                root.left.level=root.level - 1
            if root.right is not None:
                q.append(root.right)
                root.right.level = root.right + 1
        for i in sorted(dic):
            print(dic[i] , end=' ')
            



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
    print(l.height(root))
    print(l.levelOrder(root))

