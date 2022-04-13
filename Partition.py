
#creation of singly linked list
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
    def traversal(self,head):
        tempnode=head
        while(tempnode.next==None):
            print(f"({tempnode.value},-->",end="")
            tempnode=tempnode.next
    def search(self,svalue):
        tempnode=self.head
        while(tempnode is not None):
            if(tempnode.value==svalue):
                return("yes!! value found ")
            tempnode=tempnode.next
        return("value not in list!!")
    def deletenode(self,location):
        if location==0:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
        elif(location==-1):
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if(node.next==self.tail):
                            break
                        node=node.next
                    node.next=None
                    self.tail=None
        else:
            if self.head==self.tail:
                self.head=None
                self.tail-None
            else:
                node=self.head
                index=0
                while(index<location-1):
                    node=node.next
                    index+=1
                nextnode=node
                node.next=nextnode.next
    def delete_full(self):
        if self.head is None:
            print("list does not exist")
        else:
            self.head=None
            self.tail-None


def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

s1 = Slinkedlist()
s1.insertSLL(3)
s1.insertSLL(4,1)
s1.insertSLL(5,1)
s1.insertSLL(6,1)
s1.insertSLL(1)
s1.insertSLL(100,3)
print([tempnode.value for tempnode in s1])
partition(s1, 4)
print([tempnode.value for tempnode in s1])