class Node:
    def __init__(self,val=0):
        self.next=None
        self.val=val

class linked_list:
    def __init__(self) :
        self.head=None
        self.tail=None
    def insertSLL(self,val):
        node=Node(val)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def set_cir(self):
        p=self.head
        self.tail.next=self.head
        self.tail=self.head
    def isCircular(self):
        p= curr=(self.head)
        if not curr:
            return False
        while curr:
            if curr.next==p:
                return True
            elif curr.next!=None:
                curr=curr.next
            elif(curr.next==None):
                return False
        return False

l1=linked_list()
l1.insertSLL(2)
l1.insertSLL(4)
l1.insertSLL(3)   
l1.set_cir()    
print(l1.isCircular())