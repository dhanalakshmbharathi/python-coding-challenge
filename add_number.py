
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
    
    def add_number(self,l1,l2):
        carry=0
        p=Node(0)
        q=Node(0)
        p=l1.head
        q=l2.head
        while(p or q or carry):
            x=p.val if (p!=None) else 0 
            y=q.val if (q!=None) else 0 
            carry,out=divmod(x+y+carry,10)
            self.insertSLL(out)
            if(p!=None):
                p=p.next
            if(q!=None):
                q=q.next
        tempnode=self.head
        while(tempnode):
            print(tempnode.val)
            tempnode=tempnode.next



l1=linked_list()
l1.insertSLL(2)
l1.insertSLL(4)
l1.insertSLL(3)       
l2=linked_list()
l2.insertSLL(5)
l2.insertSLL(6)
l2.insertSLL(4)    
l3=linked_list()
l3.add_number(l1,l2)

