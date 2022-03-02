
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linked_list(ListNode):

    def __init__(self) :
        ListNode.__init__(self,val=0)
        self.head=None
        self.tail=None
    def insertSLL(self,val):
        node=ListNode(val)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def pairSum(self) -> int:
        current=self.head
        def getsize(head):
            count=0
            curr=head
            while(curr):
                count+=1
                curr=curr.next
            return count
        c=getsize(self.head)
        mid= c//2 
        for i in range(1,mid):
            current=current.next
        def reverseList(temp):  
            current = temp  
            prevNode = None  
            nextNode = None  
            while(current != None):  
                nextNode = current.next 
                current.next = prevNode  
                prevNode = current  
                current = nextNode  
            return prevNode;     
        revHead = reverseList(current.next)
        tempnode=self.head
        ans=0
        while(revHead):
            ans = max(ans, revHead.val + tempnode.val)
            revHead = revHead.next
            tempnode= tempnode.next
        return ans

l1=linked_list()
l1.insertSLL(5)
l1.insertSLL(4)
l1.insertSLL(2)    
l1.insertSLL(1)
print(l1.pairSum())
