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
    def find_pair(self,s):
        first=self.head
        last=self.head
        while last.next!=None:
            last=last.next
        found=False
        while(first!=last and last.next!=first):
            if (first.value+last.value)==s:
                found=True
                print((first.value,last.value))
                first=first.next
                last=last.prev
            else:
                if first.value+last.value<s:
                    first=first.next
                else:
                    last=last.prev


d=doublyLL()
d.creation(1)
d.insertion(2,-1)
d.insertion(4,-1)
d.insertion(5,-1)
d.insertion(6,-1)
d.insertion(8,-1)
d.insertion(9,-1)
print([node.value for node in d])
print(d.find_pair(7))