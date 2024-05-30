############### simple method ###############################
class BinaryTree:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if data < self.data :
            if self.left:
                self.left.insert_node(data)
            else:
                self.left= BinaryTree(data)
        else:
            if self.right:
                self.right.insert_node(data)
            else:
                self.right= BinaryTree(data)

    def inorder_printTree(self):
        if self.left:
            self.left.inorder_printTree()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_printTree()


    def pre_order_printTree(self):
        print(self.data, end=' ')
        if self.left:
            self.left.pre_order_printTree()
        if self.right:
            self.right.pre_order_printTree()

    def post_order_printTree(self):
        if self.left:
            self.left.post_order_printTree()
        if self.right:
            self.right.post_order_printTree()
        print(self.data, end=' ')

if __name__ == "__main__":
    l= BinaryTree(5)
    l.insert_node(10)
    l.insert_node(2)
    l.insert_node(1)
    l.insert_node(15)
    print('inorder',l.inorder_printTree())
    print('preorder',l.pre_order_printTree())
    print('postorder',l.post_order_printTree())


##################another method ############################
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

    #check if given tree is binary search tree or not
    # binary serarch tree should have only two child node (left and right)
    # binary serarch tree should have left < root < right condition
    # if that is not matching then it is just a binary tree not binary search tree
    
    #logic : just create inorder traverse and it will sort the array and then check if any element is smaller than 
    #previous element or not. if yes then False otherwise it is BST
    def checkIfBst(self,root):
        values=[]
        def inorder_traverse(root,values):
            if root is None:
                return
            self.traverse_inorder(root.left)
            values.append(root.data)
            self.traverse_inorder(root.right)
        inorder_traverse(root,values)
        for i in range(len(values)-1):
            if values[i] >= values[i+1]:
                return False
        return True
    
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
    print(l.checkIfBst(root))

