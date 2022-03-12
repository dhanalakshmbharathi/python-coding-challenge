from audioop import lin2adpcm


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

    def reverse(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            head = prev
        return head 
    def compute(self):
        head=self.head
        head = self.reverse(head)
        n = head.next
        curr = head
        while(n):
            if curr.val > n.val:   
                curr.next = n.next
                n = curr.next  
            else:
                curr = curr.next
                n = n.next
        head = self.reverse(head)
        tempnode=head
        while tempnode:
            print(tempnode.val)
            tempnode=tempnode.next

        return(head)



l=linked_list()
l.insertSLL(12)
l.insertSLL(15)
l.insertSLL(10)
l.insertSLL(11)
l.insertSLL(5)
l.insertSLL(6)
l.insertSLL(2)
l.insertSLL(3)
head=(l.compute())
