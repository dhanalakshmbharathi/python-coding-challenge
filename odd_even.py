class Node:
    def __init__(self,val=0):
        self.next=None
        self.val=val

class linked_list:
    def __init__(self) :
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertSLL(self,val):
        node=Node(val)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def divide(self):
        e=None
        even=None
        o=None
        odd=None
        while self.head:
            if self.head.val%2==0:
                if e ==None:
                    even=self.head
                    e=self.head
                else:
                    e.next=self.head
                    e=e.next
            else:
                if o is None:
                    o=self.head
                    odd=self.head
                else:
                    o.next=self.head
                    o=o.next
            self.head=self.head.next
        if e:
            e.next=odd
        if o:
            o.next=None
        if even:
            return even
        return odd
                
l=linked_list()
l.insertSLL(17)
l.insertSLL(15)
l.insertSLL(8)
l.insertSLL(9)
l.insertSLL(2)
l.insertSLL(4)
l.insertSLL(6)

print([node.val for node in l])
l.divide()


    