# Reverse a Linked List in groups of given size. 
from email import header


class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL():
    def __init__(self,): 
        self.head=None
        self.tail=None
    
    def insertion(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            new_node=Node(value)
            self.tail.next=new_node
            self.tail=new_node
    
    def traversal(self,head):
        tempnode=self.head
        while(tempnode is not None):
            print(f"{tempnode.value}-->",end= " ")
            tempnode=tempnode.next

    # def r_k(self,k,head=None):
    #     prev=None
    #     current=self.head
    #     index=0
    #     while(current is not None):
    #         next=current.next
    #         current.next=prev
    #         prev=current
    #         current=next
    #         index+=1
    #     if(current is not None):
    #         h.next=self.r_k(k,current)
    #     self.traversal()
    def reverse(self, head, k):
        dummy = head
        curr_head = head # curr head of group
        prev = new_head = tail = None
        count = 0 # count of current nodes
       
        while(dummy):
            count += 1
            t = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = t
           
            if(count % k == 0):
                if(tail):
                    tail.next = prev
                tail = curr_head
                curr_head = dummy
               
                if(count == k): # find head of list
                    new_head = prev 
       
        if(count % k != 0 ):
            tail.next = prev
            tail = curr_head
       
        tail.next = None
 

        tempnode=new_head
        while(tempnode is not None):
            print(f"{tempnode.value}-->",end=" ")
            tempnode=tempnode.next

                
s1=SLL()
s1.insertion(1)
s1.insertion(2)
s1.insertion(2)
s1.insertion(4)
s1.insertion(5)
s1.insertion(6)
s1.insertion(7)
s1.insertion(8)
s1.insertion(9)
s1.insertion(11)
s1.insertion(12)
s1.reverse(s1.head,4)









