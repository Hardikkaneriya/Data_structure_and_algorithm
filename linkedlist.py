class Node:
    def __init__(self, data= None , next= None):
        self.data  = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.ln = 0

    def insert(self, data):
        node= Node(data, self.head)
        self.head = node

    def delete(self):
        if not self.head:
            print("nothing to delet")
            return
        self.head= self.head.next

    def find_nth_elemenet(self,num):
        if not self.head:
            print("there is no element present")
        if  num > self.ln :
            print("out of range")
            return
        lnitr= self.head
        lstr=0
        i=0
        while i < num:
            lstr= lnitr.data
            lnitr = lnitr.next
            i+=1
        print(lstr)

    def print(self):
        if not self.head :
            print("Linkedlist is Empty")
            return
        itr = self.head
        lstr= ''
        while itr:
            lstr += str(itr.data) + ("-->" if itr.next else '')
            self.ln += 1
            itr = itr.next
        print(lstr)

if __name__ == "__main__":
    l= LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(50)
    l.insert(100)
    l.delete()
    l.insert(10)
    l.print()
    l.find_nth_elemenet(10)
