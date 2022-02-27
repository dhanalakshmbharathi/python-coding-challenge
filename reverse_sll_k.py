# Reverse a Linked List in groups of given size.



class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL():
    def __init__(self,): 
        self.head=None
        self.tail=None
    
    def insertSLL(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            new_node=Node(value)
            self.tail.next=new_node
            self.tail=new_node
    
    def traversal(self,head):
        while(head):
            print(f"{head.value}-->",end= " ")
            head=head.next
    def reverse(self, head, k):
        dummy=head
        curr_head=head
        prev=tail=new_head=None
        count=0
        while(dummy):
            count+=1
            t=dummy.next
            dummy.next=prev
            prev=dummy
            dummy=t
            if(count%k==0):
                if(tail):
                    tail.next=prev
                tail=curr_head
                curr_head=dummy
                if(count==k):
                    new_head=prev
        if(count%k!=0):
            tail.next=prev
            tail=curr_head
            tail.next=None
        tempnode=new_head
        while(tempnode):
            print(f"{tempnode.value}-->",end=" ")
            tempnode=tempnode.next
    def detect_loop_r(self):
        s,f=self.head
        k=False
        while(f and f.next):
            s=s.next
            f=f.next.next
            if s==f:
                s=self.head
                while(f.next!=)
                
s1=SLL()
s1.insertSLL(1)
s1.insertSLL(2)
s1.insertSLL(2)
s1.insertSLL(4)
s1.insertSLL(5)
s1.insertSLL(6)
s1.insertSLL(7)
s1.insertSLL(8)
s1.insertSLL(9)
s1.insertSLL(11)
s1.insertSLL(12)
print(s1.reverse(s1.head,4))
# print(reverse(s1,s1.head,4))








