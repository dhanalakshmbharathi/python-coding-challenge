from ast import While


class Node:
    def __init__(self,val=0):
        self.next=None
        self.val=val


class linked_list(Node):

    def __init__(self) :
        Node.__init__(self,val=0)
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
def getsize(head):
    tempnode=head
    count=0
    while(tempnode!=None):
        count+=1
        tempnode=tempnode.next
    return count
def find_intersection(head1,head2):
        # count1=0
        # count2=0
        # temp1=self.head
        # temp2=head2
        # while temp1!=None:
        #     count1+=1
        #     temp1=temp1.next
        # while temp2!=None:
        #     count2+=1
        #     temp2=temp2.next
        # diff=abs(count1-count2)
        # if(count1>count2):
        #     temp1=self.head
        # for i in range(diff):
        #     temp1=temp1.next
        # temp2=head2
        # while(temp1!=None):
        #     if(temp1.next==temp2.next):
        #         return temp1.next.val
        #     temp1=temp2.next
        #     temp1=temp2.next
        # else:
        #     temp2=head2
        # for i in range(diff):
        #     temp2=temp2.next
        # temp1=self.head
        # while(temp2!=None):
        #     if(temp1.next==temp2.next):
        #         return temp2.next.val
        #     temp1=temp1.next
        #     temp1=temp2.next
                    
        # return -1
    
    head1=Node(0)
    head2=Node(0)
    x=getsize(head1)
    y=getsize(head2)
    print(y)
    while(x>y):
        head1=head1.next
        x-=1
    print()
    while(y>x):
        head2=head2.next
        y-=1
    while(head1!=head2):
        head1=head1.next
        head2=head2.next
    print(head1.val)
    if head1:
        return head1.val
    return -1





l1=linked_list()
l1.insertSLL(2)
l1.insertSLL(4)
l1.insertSLL(3)
l1.insertSLL(6)
l1.insertSLL(4)       
l2=linked_list()
l2.insertSLL(5)
l2.insertSLL(6)
l2.insertSLL(4)  
find_intersection(l1.head,l2.head)