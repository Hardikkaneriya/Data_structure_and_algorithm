class Node:
    def __init__(self, data=None ):
        self.data= data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head= None

    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head= new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr= self.head
        prev= None
        while itr.next:
            itr= itr.next
            prev= itr.prev
        itr.next= Node(data)

    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def print_list(self):
        if self.head is None:
            print("data does not exist")
            return
        itr= self.head
        lstr=''
        while itr:
            lstr += str(itr.data) + ("-->" if itr.next else '')
            itr = itr.next
        print(lstr)



if __name__ == '__main__':
    l= DoublyLinkedList()
    p= DoublyLinkedList()
    l.insert_at_begining(1)
    l.insert_at_begining(10)
    l.insert_at_begining(20)
    l.print_list()
    # l.insert(2)
    p.insert_at_the_end(1)
    p.insert_at_the_end(2)
    p.insert_at_the_end(30)
    p.print_list()
