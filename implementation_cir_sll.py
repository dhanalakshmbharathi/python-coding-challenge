
class Node:
    def __init__(self,val=0):
        self.next=None
        self.val=val
class csll:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def __iter__(self):
        node= self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break
        return
    def printList(self):
        if (self.head == None):
            return
        temp = self.head
        print(temp.val ,end = " ")
        temp = temp.next
        while (temp != self.head):
            print(temp.val, end = " ")
            temp = temp.next
    def create(self,nodeval:int):
        node=Node(nodeval)
        self.next=node
        self.head=node
        self.tail=node
        return(self.__iter__())
    def insert(self,val,pos):
        if self.head:
            node=Node(val)
            if pos==0:
                node.next=self.head
                self.head=node
                self.tail.next=node
            elif pos==-1:
                node.next=self.tail.next
                self.tail.next=node
                self.tail=node
            else:
                temp=0
                tempnode=self.head
                while pos!=temp:
                    tempnode=tempnode.next
                    temp+=1
                temp2=tempnode.next
                tempnode.next=node
                node.next=temp2
        else:
            return "head value is none"
    def  Traversal(self):
        if not self.head:
            return("there is no linked list")
        else:
            tempnode=self.head
            while(tempnode):
                print(tempnode.val)
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    break
            return
    def search(self,value):
        if self.head is None:
            return "No csll"
        else:
            tempnode=self.head
            while(tempnode):
                if tempnode.val==value:
                    return "yes!!"
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    return "value doesnt exist in csll"

    def reverse(self):
        if (self.head== None):
            return None
        prev = None
        current = self.head 
        next = current.next
        current.next = prev
        prev = current
        current = next
        while (current != self.head):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head.next = prev
        self.head = prev
        return self.head
    
    def deletenode(self,pos):
        if self.head is None:
            print("No csll")
            return
        else:
            if pos==0: #del first element
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif pos==-1: #end
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempnode=self.head
                index=0
                while index<pos-1:
                    tempnode=tempnode.next
                    index+=1
                nxtnode=tempnode.next
                tempnode.next=nxtnode.next
                

l1=csll()
l1.create(1)
l1.insert(0,0)
l1.insert(4,-1)
l1.insert(2,1)
l1.insert(3,2)
# l1.Traversal()
# print(l1.search(1))
# l1.reverse()
l1.deletenode(0)
l1.deletenode(2)
l1.deletenode(-1)
print([node.val for node in l1])


