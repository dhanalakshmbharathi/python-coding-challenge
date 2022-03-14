class Node:
    def __init__(self,val=0):
        self.next=None
        self.val=val

class linked_list:
    def __init__(self) :
        self.head=None
        self.tail=None
    def insertSLL(self,val):
        node=Node(val)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def removeDuplicates(self):
        dic={}
        if self.head ==None and self.head.next is None:
            return self.head
        else:
            temp=self.head
            dic[temp.data]=1
            while temp.next!=None:
                if temp.next.data in dic:
                    temp.next=temp.next.next
                    
                else:
                    dic[temp.next.data]=1
                    temp=temp.next
        return self.head
    