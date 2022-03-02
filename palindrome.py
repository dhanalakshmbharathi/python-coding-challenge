
class Node:
    def __init__(self,data=0):
        self.next=None
        self.data=data

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
        

    def isPalindrome(self):  
        def reverseList( temp):  
            current = temp  
            prevNode = None  
            nextNode = None
            while(current != None):  
                nextNode = current.next;  
                current.next = prevNode;  
                prevNode = current;  
                current = nextNode;  
            return prevNode;      
        def getSize( head):
            count = 0
            curr_node = head
            while curr_node:
                count +=1
                curr_node = curr_node.next
            return count   
        current = self.head;  
        flag = True;  
        s = getSize(self.head)
        mid = (s//2) if(s%2 == 0) else ((s+1)//2);  
        for i in range(1, mid):  
            current = current.next;   
        revHead = reverseList(current.next);  
        tempnode=self.head
        while(tempnode != None and revHead != None):  
            if(tempnode.data != revHead.data):  
                flag = False;  
                break;  
                
            tempnode = tempnode.next;  
            revHead = revHead.next  
        return flag

l1=linked_list()
l1.insertSLL(2)
l1.insertSLL(4)
l1.insertSLL(2)
print(l1.isPalindrome())   