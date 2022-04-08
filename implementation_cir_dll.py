
class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
        self.prev=None
class CircularDoublyLinkedList:
    def __init__(self) :
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break
    #Creation of Circular Doubly Linked List
    def CreateCDL(self, nodeValue):
        node=Node(nodeValue)
        self.head=node
        self.tail=node
        node.prev=node
        node.next=node
        return "Created successfully"
    def insertcdll(self,nodeValue,pos):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            node=Node(nodeValue)
            if pos==0:
                node.next=self.head
                node.prev=self.tail
                self.tail.next=node
                self.head.prev=node
                self.head=node
            elif pos ==1 :
                node.next=self.head
                node.prev=self.tail
                self.head.prev=node
                self.tail.next=node
                self.tail=node
            else:
                tmpnode=self.head
                index=0
                while index<(pos-1):
                    tmpnode=tmpnode.next
                    index+=1
                node.next=tmpnode.next
                node.prev=tmpnode
                node.next.prev=node
                tmpnode.next=node
            return "The node has been inserted"




cdll=CircularDoublyLinkedList()
print(cdll.CreateCDL(5))
cdll.insertcdll(0,0)
cdll.insertcdll(6,1)
cdll.insertcdll(3,2)
print([node.data for node in cdll])

