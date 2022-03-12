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
    def getNthFromLast(self,n):
        # tempnode =self.head
        # size=0
        # while tempnode:
        #     tempnode=tempnode.next
        #     size+=1
        # if n>size:
        #     return -1
        # c=0
        # tempnode=self.head
        # while c<(size-n):
        #     tempnode=tempnode.next
        #     c+=1
        # return tempnode.val
        curr_node = self.head
        nth_node = self.head
        while n :
            if n and curr_node == None:
                return -1
            curr_node = curr_node.next
            n-=1
        while curr_node :
            curr_node = curr_node.next
            nth_node = nth_node.next
        return nth_node.val

        