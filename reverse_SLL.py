class Node():
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None
    
class Slinkedlist():
    def __init__(self) -> None:
        self.head =None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    #insert in linked list
    def insertSLL(self,value,location=0):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
            self.tail=new_node
        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
            elif(location==-1):
                new_node.next=None
                self.tail.next=new_node
                self.tail=new_node
            else:
                temp_node=self.head
                index=0
                while index<location-1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next
                temp_node.next=new_node
                new_node.next=nextnode
    def traversal(self):
        tempnode=self.head
        while(tempnode is not None):
            print(f"{tempnode.value}-->",end="")
            tempnode=tempnode.next
    
    def reverse(self):
        current=self.head
        prev=None
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev        
s1=Slinkedlist()
s1.insertSLL(3)
s1.insertSLL(4,1)
s1.insertSLL(5,1)
s1.insertSLL(6,1)
s1.insertSLL(1)
s1.insertSLL(100,3)
s1.traversal()
s1.reverse()
s1.traversal()


