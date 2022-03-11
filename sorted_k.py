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
    def sorted_k(self,k):
        # current=self.head
        # while (current.prev!=None and current.value<current.prev.value):
        #     temp=current.prev.prev
        #     temp2=current.prev
        #     temp3=current.next
        #     current.prev.next=temp3
        #     current.prev.prev=current
        #     current.prev=temp
        #     current.next=temp2
        #     if (temp!=None):
        #         temp.next=current
        #     if (temp3 is not None):
        #         temp3.prev=temp2
        # if(current.prev==None):
        #     self.head =current
        # return self.head.value
        current = self.head
        while (current != None):
            back = current.prev
            key = current.value
            while (back != None and key < back.value):
                back.next.value = back.value
                back = back.prev
            if (back == None):
                self.head.value = key
            else:
                back.next.value = key 
            current = current.next
        return self.head


d=doublyLL()
d.creation(3)
d.insertion(6,-1)
d.insertion(2,-1)
d.insertion(12,-1)
d.insertion(56,-1)
d.insertion(8,-1)
print([node.value for node in d])
(d.sorted_k(2))
print([node.value for node in d])


