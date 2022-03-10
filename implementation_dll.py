
class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class doublyLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next
    def creation(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        return "done!!"
    def insertion(self,value,pos):
        if self.head is None:
            return "no linkedlist"
        else:
            node=Node(value)
            if pos==0:
                node.prev=None
                node.next=self.head
                self.head.prev=node
                self.head=node
            elif pos==-1:
                node.next=None
                node.prev=self.tail
                self.tail.next=node
                self.tail=node
            else:
                index=0
                tempnode=self.head
                while index<pos-1:
                    tempnode=tempnode.next
                    index+=1
                temp1=tempnode.next
                node.next=tempnode.next
                node.prev=tempnode
                tempnode.next=node
                temp1.prev=node
    def Traversal(self):
        if self.head is None:
            return"no doubly linked list"
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.next
            return
    def reverse_trav(self):
        if self.head is None:
            return "non doubly linked list"
        else:
            tempnode=self.tail
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.prev
            return
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev
    def search(self,val):
        if self.head is None:
            return
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==val:
                    return "yes"
                tempnode=tempnode.next
            return"No"
    def deletion(self,pos):
        if self.head is None:
            return "no linkedlist"
        else:
            if pos==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif pos==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                index=0
                tempnode=self.head
                while index<pos-1:
                    tempnode=tempnode.next
                    index+=1
                currnode=tempnode.next
                tempnode.next=currnode.next
                currnode.prev=tempnode
    def deletion_dll(self):
        if self.head is None:
            print("no linked list")
        else:
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None
            




d=doublyLL()
d.creation(3)
d.insertion(0,0)
d.insertion(1,1)
d.insertion(2,2)
d.insertion(4,-1)
d.deletion(0)
print([node.value for node in d])
